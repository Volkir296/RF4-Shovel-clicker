import pyautogui
import time

seconds = 10

def timer(seconds):
    print(f"Таймер запущен на {seconds} секунд.")
    time.sleep(seconds)
    print("Время вышло!")

timer(seconds)

foodOne = '4' # Переменная для еды
foodTwo = '5' #
shovel = '6' # Переменная для лопаты

scrWidth, scrHeight = pyautogui.size()
print(scrWidth, scrHeight) # Разрешение экрана

centrW, centrH = scrWidth/2, scrHeight/2
print(centrW,centrH) # Середина экарана

pyautogui.moveTo(centrW,centrH) # Перемещение курсора по XY на центр экрана

pyautogui.click() # Клик мыши

pyautogui.press('space')

pyautogui.press(foodOne)