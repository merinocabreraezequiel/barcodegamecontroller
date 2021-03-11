#BASED ON https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
import win32gui
arraywindowsopen = []

def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        windowsopen = win32gui.GetWindowText( hwnd )
        if windowsopen != "":
            arraywindowsopen.append(windowsopen)
            print (len(arraywindowsopen), arraywindowsopen[len(arraywindowsopen)-1])

win32gui.EnumWindows( winEnumHandler, None )

windowselected = input("selecciona de la lista: ")
if int(windowselected) < len(arraywindowsopen):
    print (arraywindowsopen[int(windowselected)-1])