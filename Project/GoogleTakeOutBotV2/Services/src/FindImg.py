import pyautogui
import time
import pandas as pd

def countDown(sec = 5):
    for x in range(sec):
        time.sleep(1)
        print('waiting ' + str(x+1))

def findImgAndClick(_path, _x=10, _y=10):
    Img = pyautogui.locateOnScreen(_path, confidence=0.9)
    while Img is None:
        print('cannot find ' + _path)
        time.sleep(1)
        Img = pyautogui.locateOnScreen(_path, confidence=0.9)
    print('found ' + _path)
    pyautogui.moveTo(Img[0]+_x, Img[1]+_y)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    return Img


def findImgOnScreen(_path):
    Img = pyautogui.locateOnScreen(_path, confidence=0.9)
    while Img is None:
        print('cannot find ' + _path + ' now waiting...')
        time.sleep(1)
        Img = pyautogui.locateOnScreen(_path, confidence=0.9)
    print('found ' + _path)
    return Img
