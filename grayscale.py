#imports
import cv2 as cv

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
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #display the filter
    cv.imshow("grayscale",gray)
    cv.waitKey(1)
cv.destroyAllWindows()