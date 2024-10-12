import pyautogui
import time

flag = False


while True:
    if flag == False:
        flag = True
        time.sleep(5)
    else:
        pyautogui.keyDown('A')
        time.sleep(0.15)
        pyautogui.keyUp('A')
        pyautogui.keyDown('D')
        time.sleep(0.15)
        pyautogui.keyUp('D')


