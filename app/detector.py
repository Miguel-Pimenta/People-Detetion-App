from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_people(image):
    results = model(image)
    boxes = []

    for result in results:
        for box in result.boxes:
            if int(box.cls[0]) == 0:  # class 0 is "person" in YOLO
                coords = box.xyxy[0].tolist()  # [x1, y1, x2, y2]
                boxes.append(coords)

    return boxes