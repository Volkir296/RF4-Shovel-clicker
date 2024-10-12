import pyautogui
import time
import random


i = 5
flag = False

while True:
    if flag == False:
        flag = True
        time.sleep(i)
    else:
        pyautogui.click() # Клик мыши
        print('клик')
        time.sleep(1) #Таймер
        ##pyautogui.click() # Клик мыши
        ##print('клик')
        ##time.sleep(1) #Таймер