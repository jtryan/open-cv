
import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('images/chrome-face-watch.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('images/grand.jpg', cv2.IMREAD_GRAYSCALE)
#IMREAD_GRAYSCALE == 0
#IMREAD_COLOR == 1
#IMREAD_UNCHANGED == -1

print(img.shape)
print(img.size)
print(img.dtype)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()

cv2.imwrite('watchgray.png', img)
# matplotlib = RGB
# opencv = GBR
# MORE info -= pythonprogramming.net
