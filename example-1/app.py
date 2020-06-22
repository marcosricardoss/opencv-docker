import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.show()