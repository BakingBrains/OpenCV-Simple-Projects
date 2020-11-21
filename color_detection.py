import cv2
import numpy as np

def empty():
    pass


path = 'bottle.jpg'
cv2.namedWindow('Track Bar')
cv2.resizeWindow('Track Bar',640,240)
cv2.createTrackbar('Hue min','Track Bar',0,179,empty)
cv2.createTrackbar('Hue max','Track Bar',177,179,empty)
cv2.createTrackbar('Sat min','Track Bar',12,255,empty)
cv2.createTrackbar('Sat max','Track Bar',255,255,empty)
cv2.createTrackbar('Val min','Track Bar',0,255,empty)
cv2.createTrackbar('Val max','Track Bar',255,255,empty)



while True:
    img = cv2.imread(path)
    img = cv2.resize(img, (400, 400))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue min', 'Track Bar')
    h_max = cv2.getTrackbarPos('Hue max', 'Track Bar')
    s_min = cv2.getTrackbarPos('Sat min', 'Track Bar')
    s_max = cv2.getTrackbarPos('Sat max', 'Track Bar')
    v_min = cv2.getTrackbarPos('Val min', 'Track Bar')
    v_max = cv2.getTrackbarPos('Val max', 'Track Bar')
    print(h_min, h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('original', img)
    cv2.imshow('HSV', imgHSV)
    cv2.imshow('Mask', mask)
    cv2.imshow("Result", imgResult)
    cv2.waitKey(1)

