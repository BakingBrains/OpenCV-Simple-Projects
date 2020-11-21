import cv2

capt = cv2.VideoCapture(0)
capt.set(5,640)
capt.set(4, 480)

while True:
    sucess, img = capt.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
