from ultralytics import YOLO
import cv2
from datetime import datetime
import os
from logger import log_event

# ======================
# INIT
# ======================
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

alarm_triggered = False

# Video saving setup
save_dir = "recordings"
os.makedirs(save_dir, exist_ok=True)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None
recording = False

def start_recording():
    global out, recording
    filename = f"{save_dir}/event_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi"
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))
    recording = True

def stop_recording():
    global out, recording
    if out:
        out.release()
    recording = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated = results[0].plot()

    # ======================
    # COUNT PEOPLE
    # ======================
    person_count = 0

    for box in results[0].boxes:
        cls = int(box.cls[0])
        name = model.names[cls]
        if name == "person":
            person_count += 1

    # ======================
    # DISPLAY INFO
    # ======================
    cv2.putText(annotated, f"People: {person_count}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 255), 2)

    # ======================
    # ALERT SYSTEM
    # ======================
    if person_count > 2:
        cv2.putText(annotated, "ALERT!", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        if not alarm_triggered:
            log_event("ALERT: Crowd detected")
            start_recording()
            alarm_triggered = True

    else:
        alarm_triggered = False
        stop_recording()

    # ======================
    # SAVE VIDEO
    # ======================
    if recording:
        out.write(frame)

    # ======================
    # SHOW
    # ======================
    cv2.imshow("AI SURVEILLANCE PRO", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()