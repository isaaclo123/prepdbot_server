__author__ = "Isaac Lo"
__copyright__ = "Copyright 2015"
#PrepdBot Client

import socket
import pickle
import time
import pyautogui
from subprocess import Popen

#server IP information
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

#variables
UserName = "john"
Password = "smith"
WaitTime = 9
ChromiumBinary = "chromium-browser"

#note: these coordinates given are for a 800x600 screen
UserNameLocation = [403,192]
PasswordLocation = [387,237]
PrepdButtonLocation = [754,70]
FolderSelectLocation = [412,260]
CatchButtonLocation = [672,341]

FirstBool = True

def cut(link, FolderName):
    global UserName
    global Password
    global WaitTime
    global ChromiumBinary
    global UserNameLocation
    global PasswordLocation
    global PrepdButtonLocation
    global FolderSelectLocation
    global CatchButtonLocation
    global FirstBool

    print "Link: " + link
    print "Folder Name: " + FolderName + "\n"

    Popen([ChromiumBinary, link])
    print "went to rss link"
    time.sleep(WaitTime)

    pyautogui.moveTo(PrepdButtonLocation[0], PrepdButtonLocation[1])
    pyautogui.click()
    print "clicked on prepd button"
    time.sleep(WaitTime)

    if FirstBool == True:
        #login
        time.sleep(WaitTime)

        pyautogui.moveTo(PasswordLocation[0], PasswordLocation[1])
        pyautogui.click()
        pyautogui.typewrite(Password, interval=0.05)
        print "typed password"

        pyautogui.moveTo(UserNameLocation[0], UserNameLocation[1])
        pyautogui.click()
        pyautogui.typewrite(UserName, interval=0.05)
        print "typed username"

        pyautogui.press('enter')
        print "logged in"

        time.sleep(WaitTime)

    pyautogui.moveTo(FolderSelectLocation[0], FolderSelectLocation[1])
    pyautogui.click()
    print "clicked on folder selection"

    pyautogui.typewrite(FolderName, interval=0.05)
    pyautogui.press('enter')
    print "typed into folder selection"

    pyautogui.moveTo(CatchButtonLocation[0], CatchButtonLocation[1])
    pyautogui.click()
    time.sleep(WaitTime)
    print "caught article"

    pyautogui.press("esc")

    pyautogui.hotkey('ctrl', 'w')
    print "closed tab\n"

Popen([ChromiumBinary, "--start-maximized"])
time.sleep(WaitTime)
print "done"

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send("READY")
    data = pickle.loads(s.recv(BUFFER_SIZE))
    #[TheLink, FolderName]
    cut(data[0], data[1])
    FirstBool = False
