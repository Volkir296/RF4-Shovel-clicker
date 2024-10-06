import pyautogui
import time

# Переменные
foodOne = '4' # Переменная для еды
foodTwo = '5' # Переменная для еды 2
shovel = '6' # Переменная для лопаты
#seconds = 10 # Время для таймера'
flag = False

# 30 секунд на полном солнышке
# 4 секунды от копания до пробела


# Определение середины экрана
scrWidth, scrHeight = pyautogui.size()
print(scrWidth, scrHeight) # Разрешение экрана
centrW, centrH = scrWidth/2, scrHeight/2
print(centrW,centrH) # Середина экарана

while True:
    if flag == False:
        flag = True
        time.sleep(5)
    else:
        pyautogui.moveTo(centrW,centrH) # Перемещение курсора по XY на центр экрана
        pyautogui.click() # Клик мыши
        time.sleep(4) #Таймер
        pyautogui.press('space')
        time.sleep(1) #Таймер
        pyautogui.press(foodOne)
        pyautogui.press(foodTwo)
        time.sleep(30) #Таймер