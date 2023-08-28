from pynput.mouse import Button, Controller as MouseController
from mss import mss
import cv2
import numpy as np

class Controller:
    def __init__(self):
        self.mouse = MouseController()

    def move_mouse(self, x, y):
        self.mouse.position = (int(x), int(y))

    def left_click(self):
        self.mouse.click(Button.left)

class Vision:
    def __init__(self):
        self.template_paths = {
            "OperationComplete": "assets/OperationComplete.png",
            "RepeatButton": "assets/RepeatButton.png"
        }
        #self.templates = {k: cv2.imread(v, 0) for k, v in self.template_paths.items()}
        self.monitor = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
        self.screen = mss()

    def take_screenshot(self):
        ss = self.screen.grab(self.monitor)
        img = np.array(ss)
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        return img_gray
    
    def match_template(self, img_gray, template, threshold):
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        return loc

    def find_template(self, name, image=None):
        threshold = 0.6
        if image is None:
            image = self.take_screenshot()
        return self.match_template(image, self.templates[name], threshold)
    
m = Vision()
img = m.take_screenshot()
