import time

from utils.KeyboardMonitor import KeyboardMonitor
from utils.WindowCapture import window_capture
from ultralytics import YOLO

person_model = YOLO("models/yolov8n.pt")


def camp(_):
    img_file = f'{time.time_ns()}.jpg'

    window_capture(img_file)

    result = person_model(img_file)[0]
    xywh = None
    max_score = 0
    if result.boxes is not None:
        for i, cls_value in enumerate(result.boxes.cls.tolist()):
            if cls_value == 0:
                if result.boxes.conf.tolist()[i] > max_score:
                    max_score = result.boxes.conf.tolist()[i]
                    xywh = result.boxes.xywh[i]

    print(f'人物位置: {xywh}, {time.time()}')


class CampFunction:

    def __init__(self):
        KeyboardMonitor('v', camp)
