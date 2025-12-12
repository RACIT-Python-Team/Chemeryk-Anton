import cv2
import mediapipe as mp

mp_hands=mp.solutions.hands
hands=mp_hands.Hands()
mp_draw=mp.solutions.drawing_utils

landmark_drawing=mp_draw.DrawingSpec(color=(255,200,100),thickness=2,circle_radius=4)
connection_drawing=mp_draw.DrawingSpec(color=(0,255,0),thickness=2)

cap=cv2.VideoCapture(0)

while True:
    success,frame=cap.read()
    if not success:
        break

    frame=cv2.resize(frame,None,fx=1.7,fy=1.7)
    frame_rgb=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results=hands.process(frame_rgb)
    hand_count=0
    if results.multi_hand_landmarks:
        hand_count=len(results.multi_hand_landmarks)

        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS,landmark_drawing,connection_drawing)

    text=f"Hands detected:{hand_count}"
    text_size,_=cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX,0.8,2)
    text_x=frame.shape[1]-text_size[0]-10
    text_y=frame.shape[0]-10
    cv2.putText(frame, text, (text_x, text_y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow('Hands Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()