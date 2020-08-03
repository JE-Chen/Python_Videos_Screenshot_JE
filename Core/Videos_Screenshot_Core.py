import datetime

from Models.Screenshot_Window import Screenshot_Window
from Models.Zone_Screenshot import Zone_Screenshot
from Models.Video_Window import Video_Window

class Videos_Screenshot_Core:

    def __init__(self):
        try:
            self.Screenshot_Window=Screenshot_Window()
            self.Zone_Screenshot=Zone_Screenshot()
            self.Video_Window=Video_Window()
        except Exception as Errr:
            raise Errr
        print(datetime.datetime.now(),self.__class__,'Ready',sep=' ')
