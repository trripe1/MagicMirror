import cv2
import numpy as np
import time
import websocket
import json

# Configura la URL del WebSocket de MagicMirror
WS_URL = "ws://localhost:8080"  # Ajusta si tu MM escucha en otro puerto
try:
    ws = websocket.WebSocket()
    ws.connect(WS_URL)
except Exception as e:
    print("No se pudo conectar al WebSocket:", e)
    ws = None

cap = cv2.VideoCapture(0)  # /dev/video0, tu Krom USB
cap.set(3, 640)
cap.set(4, 480)

prev_center = None
gesture_cooldown = 1  # segundos entre gestos
last_gesture_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertimos a HSV para segmentar piel
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 30, 60], dtype=np.uint8)
    upper_skin = np.array([20, 150, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    mask = cv2.GaussianBlur(mask, (5,5), 0)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        cnt = max(contours, key=lambda x: cv2.contourArea(x))
        if cv2.contourArea(cnt) > 1000:
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                center = (cX, cY)

                cv2.circle(frame, center, 7, (0,0,255), -1)

                if prev_center and (time.time() - last_gesture_time > gesture_cooldown):
                    dx = center[0] - prev_center[0]
                    if dx > 40:
                        print("Swipe DERECHA")
                        if ws: ws.send(json.dumps({"gesture": "RIGHT"}))
                        last_gesture_time = time.time()
                    elif dx < -40:
                        print("Swipe IZQUIERDA")
                        if ws: ws.send(json.dumps({"gesture": "LEFT"}))
                        last_gesture_time = time.time()

                prev_center = center

    #cv2.imshow("Hand Detection", frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
     #   break

cap.release()
cv2.destroyAllWindows()
if ws: ws.close()
