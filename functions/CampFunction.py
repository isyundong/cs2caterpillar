import time

from utils.KeyboardMonitor import KeyboardMonitor
from ultralytics import YOLO

person_model = YOLO("yolov8n.pt")


def camp(_):
    # person_model.cuda()
    result = person_model("C:\\Users\yundong.zhang\\Downloads\\1.jpg")[0]
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
