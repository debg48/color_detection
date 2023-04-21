import cv2

cap = cv2.VideoCapture(0)

# hd resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while True: 
    _,frame = cap.read()

    hsv_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    # center pixel to be taken for detection

    height,width,_=frame.shape

    # calculating center of the frame

    cx = int(width/2)
    cy = int(height/2)

    #pick pixel value

    pixel_center = hsv_frame[cy,cx]
    print(pixel_center)
    cv2.circle(frame,(cx,cy),5,(225,0,0),3)

    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)

    # press s key to break out of loop
    if key == 27 :
        break

cap.release()
cv2.destroyAllWindows()
