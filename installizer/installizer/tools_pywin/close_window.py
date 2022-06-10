import win32process
import win32gui
import win32api
import win32con
import time


def close_window():
    # Get the window
    hwnd = win32gui.GetForegroundWindow()

    # Get the window's process id's
    t, p = win32process.GetWindowThreadProcessId(hwnd)

    # Ask window nicely to close
    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

    # Allow some time for app to close
    time.sleep(1)

    # If app didn't close, force close
    try:
        handle = win32api.OpenProcess(win32con.PROCESS_TERMINATE, 0, p)
        if handle:
            win32api.TerminateProcess(handle, 0)
            win32api.CloseHandle(handle)
    except:
        pass
