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
    hue_value=pixel_center[0]
    s_value=pixel_center[1]
    v_value=pixel_center[2]

    # identifying the color based on hue

    color = "UNDEFINED"
    if hue_value < 5 :
        color = "RED"
    elif hue_value < 22 :
        color = "ORANGE"
    elif hue_value < 34 :
        color = "YELLOW" 
    elif hue_value < 80 :
        color = "GREEN"
    elif hue_value < 130 :
        color = "BLUE"
    elif hue_value < 143 :
        color = "VIOLET"
    elif hue_value < 168 :
        color = "PINK"
    else :
        color="RED"
        

    pixel_center_bgr=frame[cy,cx]
    b,g,r = int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])

    cv2.putText(frame,color,(10,70),0,1.5,(b,g,r),2)
    cv2.circle(frame,(cx,cy),5,(25,25,25),3)

    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)

    # press s key to break out of loop
    if key == 27 :
        break

cap.release()
cv2.destroyAllWindows()
