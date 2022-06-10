import win32gui


def window_name():
    hwnd = win32gui.GetForegroundWindow()
    name = win32gui.GetWindowText(hwnd)
    return name
