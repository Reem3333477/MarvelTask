import cv2
import numpy as np
import matplotlib.pyplot as plt

print("Kolo tamam ")


#LOAD IMG IN GRAY SCALE

marvel = cv2.imread("Marvel (2).jpg", cv2.IMREAD_GRAYSCALE)

print("SHAPE:", marvel.shape)
print("DTYPE:", marvel.dtype)
print("MINiMUM:", marvel.min())
print("MAXIMUM:", marvel.max())

#3ard elsora 
plt.imshow(marvel, cmap="gray")
plt.axis("off")
plt.show()

#Exercise 2

color = cv2.imread("Marvel (2).jpg" , cv2.IMREAD_COLOR)
gray = cv2.imread("Marvel (2).jpg" , cv2.IMREAD_GRAYSCALE)
unchanged = cv2.imread("Marvel (2).jpg" , cv2.IMREAD_UNCHANGED)

print("COLOR:", color.shape, color.dtype)
print("GRAYSCALE:", gray.shape, gray.dtype)
print("UNCHANGED:", unchanged.shape, unchanged.dtype)