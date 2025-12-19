import cv2
import numpy as np


frame = None

def get_hsv_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv_value = hsv_frame[y, x]
        
        print(f"BGR колір: {frame[y, x]}")
        print(f"HSV колір: {hsv_value}")
        print("-" * 30)

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', get_hsv_color)

cap = cv2.VideoCapture(0) 

print("Натисніть ліву кнопку миші на об'єкті для отримання його HSV-значень.")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow('Image', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Color Mask', mask)
    cv2.imshow('Filtered Result', result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()