# Countour Detection

# Libraries

import cv2
from cv2 import threshold
from matplotlib.pyplot import contour, gray
import numpy as np

# Reading image
image= cv2.imread("inputImages\coin.jpg")

# converting input image to grayscale image
grayImage=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

# finding Countours and Drawing them
# binary thresholding
ret, thresh = cv2.threshold(grayImage,100,100,cv2.THRESH_BINARY)

# drawing countour Uing CHAIN_APPROX_NONE
contour, hierarchy =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

# drawing
imageCopy=image.copy()
cv2.drawContours(imageCopy,contour,-1,(0,242,0),2,cv2.LINE_AA)

# drawing countour using CHAIN_APPROX_SIMPLE
contourSecond,hierarchySecond=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 

# drwaing
imageCopySecond=image.copy()
cv2.drawContours(imageCopySecond,contourSecond,-1,(100,424,255),2,cv2.LINE_AA)

cv2.imshow("image", image)
cv2.imshow("gray image", grayImage)
cv2.imshow("binary image", thresh)
cv2.imshow("contour image NONE", imageCopy)
cv2.imshow("contour image SIMPLE", imageCopySecond)

# cv2.imwrite("outputImages/image.jpg",image)
# cv2.imwrite("outputImages/grayImage.jpg",grayImage)
# cv2.imwrite("outputImages/binaryImage.jpg",thresh)
# cv2.imwrite("outputImages/countourNONE.jpg",imageCopy)
# cv2.imwrite("outputImages/countourSIMPLE.jpg",imageCopySecond)


cv2.waitKey(0)
