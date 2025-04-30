import cv2
import numpy as np

image1 = cv2.imread('input1.jpg')
image2 = cv2.imread('input2.jpg')

weightedSum = cv2.addWeighted(image1, 0.5, image2,0.4, 0)

cv2.imshow('Weighted Image', weightedSum)

cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2

img = cv2.imread("pika.png",1)
cv2.imshow("Original Image", img)

resized = cv2.resize(img, (500, 250))
cv2.imshow("reducedImage", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import numpy as np
  
image = cv2.imread("pika.png", 1) 
  
kernel = np.ones((5, 5), np.uint8)

image = cv2.erode(image, kernel) 
cv2.imshow("Eroded Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

image = cv2.imread("pika.png")

cv2.imshow('Original Image', image)
cv2.waitKey(0)

Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)

median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)

bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

img = cv2.imread("pika.png")
borderedImage = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = 1)

cv2.imshow("Bordered Image", borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

img = cv2.imread("img3.png")
borderedImage = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT, value = 1)

cv2.imshow("Bordered Image", borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()