import cv2
from rolo.yolo_wrapper import YOLODetector
from rolo.rolo_sim import RoloTracker

video_path = 'data/cars_video.mp4'
yolo_cfg = 'yolo/yolov3.cfg'
yolo_weights = 'yolo/yolov3.weights'
yolo_names = 'yolo/coco.names'

yolo = YOLODetector(yolo_cfg, yolo_weights, yolo_names)
tracker = RoloTracker()

cap = cv2.VideoCapture(video_path)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    detections = yolo.detect(frame)
    if detections:
        # Track the first detection
        x, y, w, h, conf, label = detections[0]
        tracked_box = tracker.track((x, y, w, h))
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} {conf:.2f}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("ROLO-style Tracker", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
