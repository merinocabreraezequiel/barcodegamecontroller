import win32gui
import win32con
import win32api
import json
from time import sleep

arraywindowsopen = []
windowtosend = ""
hwndChild = ""
defaultbarcodes = '{ "w":"qL0aX0cP1mC9vQ9w", "a":"nV2pZ0gJ8hN9zX0j", "s":"cR4zK4tX2dZ4sQ9j", "d":"cR4zK4tX2dZ4sQ9j", "_":"aA9iI6yB7bR2pO4j"}'
usedbarcodes = json.loads(defaultbarcodes)

def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        windowsopen = win32gui.GetWindowText( hwnd )
        if windowsopen != "":
            arraywindowsopen.append(windowsopen)
            print (len(arraywindowsopen), arraywindowsopen[len(arraywindowsopen)-1])

def run():
    global hwndChild
    win32gui.EnumWindows( winEnumHandler, None )

    windowselected = input("Select Window ID: ")
    if int(windowselected) < len(arraywindowsopen):
        print ('Selected Window: ', arraywindowsopen[int(windowselected)-1],'\n')
        windowtosend = arraywindowsopen[int(windowselected)-1]

    hwndMain = win32gui.FindWindow(None, windowtosend)
    hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)

    sendControl()

def sendControl():
    while True:
        codereaded = input('Enter your input:')
        if codereaded == usedbarcodes["w"]:
            temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x77, 0)
            print ('w\n')
        elif codereaded == usedbarcodes["a"]:
            temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x61, 0)
            print ('a\n')
        elif codereaded == usedbarcodes["s"]:
            temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x73, 0)
            print ('s\n')
        elif codereaded == usedbarcodes["d"]:
            temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x64, 0)
            print ('d\n')
        elif codereaded == usedbarcodes["_"]:
            temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x20, 0)
            print ('_\n')

if __name__ == '__main__':
    run()