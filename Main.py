import cv2
import numpy as np
from matplotlib import pyplot as plt


print("Program uruchomiony")

# odczytanie obrazka
img = cv2.imread('obrazek.png')

# Zamiana obrazu na stopnie szarosci
obrazek_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# drukowanie histogramu
print("Histogram przed normalizacja")
plt.hist(obrazek_gray.ravel(), 256, [0, 256])
plt.show()

# Normalizacja histogramu
equal = cv2.equalizeHist(obrazek_gray)

# drukowanie histogramu
plt.hist(equal.ravel(), 256, [0, 256])
plt.show()

# zmiana przestrzeni barw na HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('Obraz HSV', img_hsv)

# Progowanie; wykrycie pikseli czerwonych
ret, img_bin1 = cv2.threshold(img_hsv, 254, 255, cv2.THRESH_BINARY)
cv2.imshow('Piksele czerwone', img_bin1)
cv2.waitKey(0)

# Zapisanie obrazu
cv2.imwrite('obrazek_wyjscie.jpg', img_bin1)
