import threading
import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab


class Video_Window(threading.Thread):

    def __init__(self):
        super().__init__()
        self.toplist, self.winlist = [], []
        self.setDaemon(True)
        self.Record = True

# ---------------------------------------------------------------------------------------------
    def run(self) -> None:
        print('Start Record')
        width, height = pyautogui.size()
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        video = cv2.VideoWriter('test.avi', fourcc, 25, (width, height))
        while self.Record:
            img_rgb = ImageGrab.grab()
            img_bgr = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2BGR)
            video.write(img_bgr)
            #cv2.imshow('recoding',img_bgr) This will screenshot self
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    a=Video_Window()
    a.run()
