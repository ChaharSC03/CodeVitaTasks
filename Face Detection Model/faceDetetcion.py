import cv2

#input Image
inputImage = cv2.imread("inputImages\sample1.jpg")

#loading cascade file
faceCascade = cv2.CascadeClassifier('cascade\haarcascade_frontalface_default.xml')


face= faceCascade.detectMultiScale(inputImage,1.1,4)

# dwaring rectangle for detected faces
for (x,y,w,h) in face:
    cv2.rectangle(inputImage,(x,y),(x+w,y+h),(255,15,155),2)


cv2.imshow("Face Detected",inputImage)
cv2.imwrite("outputImages/FaceDetected.jpg",inputImage)

cv2.waitKey(0)


