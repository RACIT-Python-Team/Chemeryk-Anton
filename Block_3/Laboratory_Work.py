import cv2
import numpy as np

cap=cv2.VideoCapture(0)
lower_blue=np.array([90, 50, 50])
upper_blue=np.array([130, 255, 255])

while True:
    ret,frame=cap.read()
    if not ret:
        break
    
    
    hsv_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv_frame, lower_blue, upper_blue)
    result=cv2.bitwise_and(frame, frame, mask=mask)
    
    contours, _=cv2.findContours(mask.copy(), 
                                   cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) > 0:
        largest_contour=max(contours, key=cv2.contourArea)

        if cv2.contourArea(largest_contour) > 200:
            M=cv2.moments(largest_contour)

        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            
            cv2.circle(frame, (cX, cY), 7, (205, 255, 0), -1)

            
            cv2.putText(frame, f"X: {cX}, Y: {cY}",
                        (cX + 10, cY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 255, 255), 2)

    
    #cv2.imshow('Image', frame) # Оригінальний кадр
    cv2.imshow('Object Tracking', frame) # Центр синього об'єкта
    #cv2.imshow('Mask', mask) # Маска кольору
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break