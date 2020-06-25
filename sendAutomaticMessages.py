# prerequisite: install python, pyautogui in your system
# to run in linux, type: 'python send.py' in your terminal
# for window, follow the link: https://www.wikihow.com/Use-Windows-Command-Prompt-to-Run-a-Python-File
# and then put you mouse, where you want to send the messeges

import pyautogui
from time import sleep
from random import randint

x = 30   #how many messages you want to send

# add any messages you like to send
def getmessage():
    nameList = ["I love you, ", "I miss you, ", "You're sweet, ", "You're too good, "]
    rand_name = nameList[randint(0, len(nameList) - 1)]
    return rand_name

# add how you like to address his/her
def getname():
    nameList = ["Princess", "my girl", "Baby", "Queen"]
    rand_name = nameList[randint(0, len(nameList) - 1)]
    return rand_name

while True:
    pyautogui.typewrite(f"{getmessage()}")
    sleep(.200)
    pyautogui.typewrite(f"{getname()}")
    sleep(.100)
    pyautogui.typewrite("\n")
    sleep(.5)
    
    x = x - 1
    
    if x == 0:       
        break
