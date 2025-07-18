import cv2

class YOLODetector:
    def __init__(self, config_path, weights_path, names_path):
        self.net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
        self.classes = open(names_path).read().strip().split("\n")
        self.layer_names = self.net.getLayerNames()
        self.output_layers = [self.layer_names[i - 1] for i in self.net.getUnconnectedOutLayers().flatten()]

    def detect(self, frame):
        height, width = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), swapRB=True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.output_layers)

        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = scores.argmax()
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append((x, y, w, h, confidence, self.classes[class_id]))
        return boxes
