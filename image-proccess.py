import numpy as np
import tkinter as tk
from tkinter import filedialog
from matplotlib import pyplot as plt
import cv2

def sobel_operator(image, axis='x', ksize=3):
    if axis == 'x':
        kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    elif axis == 'y':
        kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    else:
        raise ValueError("Axis must be 'x' or 'y'.")

    return cv2.filter2D(image, cv2.CV_64F, kernel)

def sobel_operator2(image, axis='x', ksize=3):
    if axis == "x":
        kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    elif axis == "y":
        kernel = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    else:
        raise ValueError("Axis must be 'x' or 'y'.")
    
    return cv2.filter2D(image, cv2.CV_64F, kernel)

def sobel_operator3(image, axis='x', ksize=5):
    if axis == "x":
        kernel = np.array([
    [-1, -2, 0, 2, 1],
    [-4, -8, 0, 8, 4],
    [-6, -12, 0, 12, 6],
    [-4, -8, 0, 8, 4],
    [-1, -2, 0, 2, 1]
])
    elif axis == "y":
        kernel = np.array([
    [1, 4, 6, 4, 1],
    [2, 8, 12, 8, 2],
    [0, 0, 0, 0, 0],
    [-2, -8, -12, -8, -2],
    [-1, -4, -6, -4, -1]
])
    else:
        raise ValueError("Axis must be 'x' or 'y'.")
    
    return cv2.filter2D(image, cv2.CV_64F, kernel)

def sobel_operator4(image, axis='x', ksize=5):
    if axis == "x":
        kernel = np.array([
        [2,2,4,2,2],
        [1,1,2,1,1],
        [0,0,0,0,0],
        [-1,-1,-2,-1,-1],
        [-2,-2,-4,-2,-2]
    ])
    elif axis == "y":
         kernel = np.array([
        [-2,-1,0,1,2],
        [-2,-1,0,1,2],
        [-4,-2,0,2,4],
        [-2,-1,0,1,2],
        [-2,-1,0,1,2]
    ])
    else:
        raise ValueError("Axis must be 'x' or 'y'.")

    return cv2.filter2D(image, cv2.CV_64F, kernel)


def laplacian_operator(image, kernel):
    return cv2.filter2D(image, cv2.CV_64F, kernel)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        if image is not None:
            process_image(image)
        else:
            print(f"Hata: Görüntü okunamadı - {file_path}")
    else:
        print("Dosya seçilmedi.")

def process_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Sobel için farklı kernel boyutları
    sobel_magnitude_3 = sobel_operator(gray_image, ksize=3)
    sobel_magnitude_5 = sobel_operator3(gray_image, ksize=5)
    sobel2_magnitude_3 = sobel_operator2(gray_image, ksize=3)
    sobel2_magnitude_5 = sobel_operator4(gray_image, ksize=5)

    # Laplacian için farklı kernel matrisleri
    laplacian_3 = laplacian_operator(gray_image, np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]))
    laplacian_5 = laplacian_operator(gray_image, np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]]))
    laplacian_7 = laplacian_operator(gray_image, np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]))
    laplacian_9 = laplacian_operator(gray_image, np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]]))
   

    # Arayüzü büyüt
    plt.figure(figsize=(16, 10))

    # Görüntüyü görselleştir
    plt.subplot(331), plt.imshow(gray_image, cmap='gray'), plt.title('Original Image')

    # Sobel Edge Detection (ksize=3 matriks 1)
    plt.subplot(332), plt.imshow(sobel_magnitude_3, cmap='gray'), plt.title('Sobel Edge Detection first matrix')
    plt.subplot(333), plt.imshow(laplacian_3, cmap='gray'), plt.title('Laplacian Edge Detection first matrix')

    # Sobel Edge Detection (ksize=3 matriks 2)
    plt.subplot(334), plt.imshow(sobel_magnitude_5, cmap='gray'), plt.title('Sobel Edge Detection third matrix')
    plt.subplot(335), plt.imshow(laplacian_5, cmap='gray'), plt.title('Laplacian Edge Detection second matrix')

    # Sobel Edge Detection (ksize=5 matriks 1)
    plt.subplot(336), plt.imshow(sobel2_magnitude_3, cmap='gray'), plt.title('Sobel Edge Detection second matrix')
    plt.subplot(337), plt.imshow(laplacian_7, cmap='gray'), plt.title('Laplacian Edge Detection third matrix')

    # Sobel Edge Detection (ksize=5 matriks 2)
    plt.subplot(338), plt.imshow(sobel2_magnitude_5, cmap='gray'), plt.title('Sobel Edge Detection fourth matrix')
    plt.subplot(339), plt.imshow(laplacian_9, cmap='gray'), plt.title('Laplacian Edge Detection fourth matrix')

    # Resimlerin boyutunu ayarla
    for i in range(1, 10):
        plt.subplot(3, 3, i), plt.xticks([]), plt.yticks([])
        

    plt.subplots_adjust(wspace=0.25, hspace=0.25)  # Alt grafikler arası uzaklık ayarla
    plt.show()
  

# Tkinter arayüzü oluştur
root = tk.Tk()
root.title("Edge Detection App")

# Arayüzü ortala
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
root.geometry("+{}+{}".format(positionRight, positionDown))

# Arayüzü büyütme
root.resizable(width=True, height=True)

#arayüzün basic boyutunu ayarla
root.geometry("1000x350")




#dosya açmadan önce başlık ekle
label = tk.Label(root, text="Görüntü işleme uygulaması",bg="#add8e6")
label.pack()

#aşşağıya açıklama ekle açıklama programın ne işe yaradığını söyleisn
label = tk.Label(root, text="Seçtiğiniz dosya üzerinde sobel ve laplacian filtreleri kullanarak kenar bulma işlemi yapar.",bg="#add8e6")
label.pack()

label = tk.Label(root, text="Sobel filtresi için farklı kernel boyutları kullanılmıştır. Kullanılan kernel boyutları 3 ve 5'tir. Kullanılan kernel matrisleri:",bg="#add8e6")
label.pack()
#kullanılan kernel matrislerini yaz
label = tk.Label(root, text="1. [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]] ve [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]",bg="#add8e6")
label.pack()
label = tk.Label(root, text="2. [[1, 1, 1], [1, -8, 1], [1, 1, 1]] ve [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]",bg="#add8e6")
label.pack()
label = tk.Label(root, text="3. [[-1,-2,0,2,1],[-4,-8,0,8,4],[-6,-12,0,12,6],[-4,-8,0,8,4],[-1,-2,0,2,1]] ve [[1,4,6,4,1],[2,8,12,8,2],[0,0,0,0,0],[-2,-8,-12,-8,-2],[-1,-4,-6,-4,-1]],",bg="#add8e6")
label.pack()
label = tk.Label(root, text="4. [[2,2,4,2,2],[1,1,2,1,1],[0,0,0,0,0],[-1,-1,-2,-1,-1],[-2,-2,-4,-2,-2]] ve [[-2,-1,0,1,2],[-2,-1,0,1,2],[-4,-2,0,2,4],[-2,-1,0,1,2],[-2,-1,0,1,2]]",bg="#add8e6")
label.pack()

label = tk.Label(root, text="Laplacian filtresi için farklı kernel matrisleri kullanılmıştır. Kullanılan kernel matrisleri:",bg="#add8e6")
label.pack()
#kullanılan kernel matrislerini yaz
label = tk.Label(root, text="1. [[0, 1, 0], [1, -4, 1], [0, 1, 0]]",bg="#add8e6")
label.pack()
label = tk.Label(root, text="2. [[1, 1, 1], [1, -8, 1], [1, 1, 1]]",bg="#add8e6")
label.pack()
label = tk.Label(root, text="3. [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]",bg="#add8e6")
label.pack()
label = tk.Label(root, text="4. [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]",bg="#add8e6")
label.pack()

#araya boşluk ekle
label = tk.Label(root, text="", bg="#add8e6")
label.pack()
#dosya açma butonu ekle ve butona renk ver
button = tk.Button(root, text="Dosya Aç", command=open_file, bg="#d3d3d3")
button.pack()
#arka plan rengini mavi yap
root.configure(bg='#add8e6')


# Uygulamayı başlat
root.mainloop()
