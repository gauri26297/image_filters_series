#imports
import cv2 as cv
import numpy as np

#capture the image stream from available camera
cap = cv.VideoCapture(0)

#make sure camera permissions are given
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    #Capture frame
    ret, frame = cap.read()
    #if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame, Exiting ...")
        break
    
    #actual filter works here
    #bilateral filter for color smoothing
    frame1 = cv.bilateralFilter(frame, 9, 300, 300)
    #get edges more defined using edge detection mask
    edges = cv.adaptiveThreshold(cv.medianBlur(cv.cvtColor(frame,cv.COLOR_BGR2GRAY), 3), 255, 
  cv.ADAPTIVE_THRESH_MEAN_C, 
  cv.THRESH_BINARY, 15, 15)
    #where there is no image, keep the colors and keep the pixels black otherwise.
    cartoonImage = cv.bitwise_and(frame1, frame1, mask=edges)
    
    #display the filter
    cv.imshow("cartoon",cartoonImage)
    cv.waitKey(1)
cv.destroyAllWindows()