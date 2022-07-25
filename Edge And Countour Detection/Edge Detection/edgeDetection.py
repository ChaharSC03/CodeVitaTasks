# Edge Detection

# Libraries
import cv2
from matplotlib import image
import numpy as np

# reading image input
image= cv2.imread("inputImages\coin.jpg", cv2.IMREAD_COLOR)
grayImage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurImage=cv2.GaussianBlur(grayImage,(3,3),0)

# Sobel Filter to detect edges

sobelHorizontal= cv2.Sobel(blurImage,cv2.CV_64F,1,0,ksize=5)
sobelVertical= cv2.Sobel(blurImage,cv2.CV_64F,0,1,ksize=5)
sobel= cv2.Sobel(image,cv2.CV_64F,1,1,ksize=5)

# Canny Edge Detection
cannyEdge=cv2.Canny(blurImage,threshold1=100,threshold2=200)

# Showing images
cv2.imshow("img",image)
cv2.imshow("img gray",grayImage)
cv2.imshow("Sobel horizontal",sobelHorizontal)
cv2.imshow("Sobel Vertical",sobelVertical)
cv2.imshow("Sobel",sobel)
cv2.imshow("Canny Edge",cannyEdge)

# cv2.imwrite("outputImages/imgae.jpg",image)
# cv2.imwrite("outputImages/grayImgae.jpg",grayImage)
# cv2.imwrite("outputImages/sobelHorizontal.jpg",sobelHorizontal)
# cv2.imwrite("outputImages/sobelVertical.jpg",sobelVertical)
# cv2.imwrite("outputImages/sobel.jpg",sobel)
# cv2.imwrite("outputImages/cannyEdge.jpg",cannyEdge)

cv2.waitKey(0)
