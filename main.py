import cv2

cap = cv2.VideoCapture(0)

_,frame = cap.read()

cv2.imshow("Frame",frame)
cv2.waitKey(0)