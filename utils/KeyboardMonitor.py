from enum import Enum
from threading import Thread

import keyboard


class KeyboardMonitor:

    def __init__(self, hotkey, hotkey_callback):
        keyboard.on_press_key(hotkey, hotkey_callback)
        Thread(None, keyboard.wait()).start()


