import win32gui
import win32con
import win32api
from time import sleep

hwndMain = win32gui.FindWindow("Notepad", "test: Bloc de notas")
hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)

while True:
    codereaded = input('Enter your input:')
    if codereaded == "qL0aX0cP1mC9vQ9w":
        temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x77, 0)
        print ('w\n')
    elif codereaded == "nV2pZ0gJ8hN9zX0j":
        temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x61, 0)
        print ('a\n')
    elif codereaded == "bZ6rN6xU4fC4wH2s":
        temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x73, 0)
        print ('s\n')
    elif codereaded == "cR4zK4tX2dZ4sQ9j":
        temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x64, 0)
        print ('d\n')
    elif codereaded == "aA9iI6yB7bR2pO4j":
        temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x20, 0)
        print ('_\n')

