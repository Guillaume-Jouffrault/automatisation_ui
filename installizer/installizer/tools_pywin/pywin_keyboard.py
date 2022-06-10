import win32con
import win32api
import time


def press_key(nb):
    time.sleep(0.7)
    win32api.keybd_event(nb, 0, 0, 0)
    win32api.keybd_event(nb, 0, win32con.KEYEVENTF_KEYUP, 0)
