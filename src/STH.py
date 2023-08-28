from pynput.mouse import Button, Controller as MouseController

class Controller:
    def __init__(self):
        self.mouse = MouseController()

    def move_mouse(self, x, y):
        self.mouse.position = (int(x), int(y))

    def left_click(self):
        self.mouse.click(Button.left)

