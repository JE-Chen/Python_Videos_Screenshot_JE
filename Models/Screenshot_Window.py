import ctypes
import ctypes.wintypes
import win32gui
from PIL import ImageGrab


class Screenshot_Window():

    def __init__(self):
        self.toplist, self.winlist = [], []

    def Enum_cb(self, hwnd, results):
        self.winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

    def EnumWindows(self, Window_Name):
        win32gui.EnumWindows(self.Enum_cb, self.toplist)
        window = [(hwnd, title) for hwnd, title in self.winlist if Window_Name in title.lower()]
        window = window[0]
        hwnd = window[0]
        return hwnd

    def get_window_rect(self, hwnd):
        try:
            f = ctypes.windll.dwmapi.DwmGetWindowAttribute
        except WindowsError:
            f = None
        if f:
            rect = ctypes.wintypes.RECT()
            DWMWA_EXTENDED_FRAME_BOUNDS = 9
            f(ctypes.wintypes.HWND(hwnd),
              ctypes.wintypes.DWORD(DWMWA_EXTENDED_FRAME_BOUNDS),
              ctypes.byref(rect),
              ctypes.sizeof(rect)
              )
            return rect.left, rect.top, rect.right, rect.bottom

    # 實際截圖並顯示
    def Show_Image(self, Window_Name):
        hwnd = self.EnumWindows(Window_Name)
        win32gui.SetForegroundWindow(hwnd)
        bbox = self.get_window_rect(hwnd)
        img = ImageGrab.grab(bbox)
        img.show()

# ----------------------------------------------------------------------------------------------
    # 取得當前視窗截圖
    def Get_Now_Window_Title_Picture(self):
        tempWindowName = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if (tempWindowName == win32gui.GetWindowText(win32gui.GetForegroundWindow())):
            x = list(tempWindowName.split())
            if (x == None or x == []):
                pass
            else:
                x = str(x[len(x) - 1]).lower()
                hwnd = self.EnumWindows(x)
                win32gui.SetForegroundWindow(hwnd)
                bbox = self.get_window_rect(hwnd)
                img = ImageGrab.grab(bbox)
                img.show()
        else:
            tempWindowName = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            # do what you want

# ----------------------------------------------------------------------------------------------
    # 取得當前所有視窗名
    def Window_enum_handler(self, hwnd, resultList):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
            resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

    def Get_app_list(self, handles=[]):
        mlst = []
        win32gui.EnumWindows(self.Window_enum_handler, handles)
        for handle in handles:
            mlst.append(handle)
        return mlst

    def Show_App_List(self):
        appwindows = self.Get_app_list()
        for i in appwindows:
            print(i)

# ----------------------------------------------------------------------------------------------
