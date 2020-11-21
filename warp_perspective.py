import cv2
import numpy as np

img = cv2.imread('bottle.jpg')
img = cv2.resize(img,(400, 400))

width, height = 200, 300
pts1 = np.float32([[100, 200], [300,188],[154,482],[352,400]])
pts2 = np.float32([[0,0], [width,0],[0, height], [width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgout = cv2.warpPerspective(img, matrix, (width, height))


cv2.imshow('Image', img)
cv2.imshow('Output', imgout)

cv2.waitKey(0)