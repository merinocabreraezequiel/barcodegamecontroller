import win32gui
import win32con
import win32api
import os
import json
from time import sleep

arraywindowsopen = []
windowtosend = ""
hwndChild = ""
usedbarcodes = ""

def createprofile():
    global usedbarcodes
    if input("Do you want to use a default profile: ") != "y":
        newprofile = "{"
        newControl = newBarcode = addmore = ""
        while addmore != "n":
            newControl = input("Chose a key: ")
            newBarcode = input("Chose a barcode to asing: ")
            addmore = input("Add another control (y/n): ")
            if addmore == "y":
                newprofile+="\""+newBarcode+"\":\""+newControl+"\","
            else:
                newprofile+="\""+newBarcode+"\":\""+newControl+"\""
        newprofile +="}"
        if input("Do you want to save it on a file: ") == "y":
            if not os.path.exists('profiles'):
                os.makedirs('profiles')
            filenametosave = input("Choose a json profile name: ")
            with open('profiles/'+filenametosave+'.json', 'w') as outfile:
                json.dump(newprofile, outfile)
        print (newprofile)
        usedbarcodes = json.loads(newprofile)
    else:
        defaultbarcodes = '{ "qL0aX0cP1mC9vQ9w":"w", "nV2pZ0gJ8hN9zX0j":"a", "cR4zK4tX2dZ4sQ9j":"s", "cR4zK4tX2dZ4sQ9j":"d", "aA9iI6yB7bR2pO4j":" "}'
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
    global usedbarcodes
    global hwndChild
    while True:
        codereaded = input('Enter your input:')
        if codereaded in usedbarcodes:
            temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, int(hex(ord(usedbarcodes[codereaded])), 0), 0)

if __name__ == '__main__':
    createprofile()
    run()