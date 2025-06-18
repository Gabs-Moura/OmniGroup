import numpy as np
import mss

class WindowCapture:

    # constructor
    def __init__(self, window_name="", size=(818, 640), origin=(0, 0)):
        self.size = size
        self.origin = origin
        self.window_name = window_name
        self.w = self.size[0]
        self.h = self.size[1]
        self.cropped_x = 0
        self.cropped_y = 0
        self.offset_x = self.origin[0]
        self.offset_y = self.origin[1]

    def get_screenshot(self):
        with mss.mss() as sct:
            monitor = {
                "top": self.origin[1],
                "left": self.origin[0],
                "width": self.size[0],
                "height": self.size[1]
            }
            img = np.array(sct.grab(monitor))
            img = img[...,:3] 
            img = np.ascontiguousarray(img)
            return img

    def list_window_names(self):
        print("Listing window names is not supported on macOS with mss.")

    def get_screen_position(self, pos):
        return (pos[0] + self.offset_x, pos[1] + self.offset_y)