import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
numPlateCascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
minArea = 500
color = (255,0,255)
count=0

capt = cv2.VideoCapture(0)
capt.set(3, frameWidth)
capt.set(4, frameHeight)
capt.set(10, 150)


while True:
    sucess, img = capt.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = numPlateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 2)
            cv2.putText(img, "Number Plate",(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,color,2)

            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow('ROI', imgRoi)


    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF==ord('s'): #press s to save the Roi
        cv2.imwrite("Scanned " +str(count)+ ".jpg", imgRoi)
        cv2.rectangle(img, (0,200),(640,300),(0,255,0), cv2.FILLED)
        cv2.putText(img, "Number Plate Saved",(150,265), cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count+=1
