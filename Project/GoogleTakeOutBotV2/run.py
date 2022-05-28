from PIL import Image
import os
import time
import pyautogui
import pandas as pd
from datetime import datetime
import sys
sys.path.append("Services/src")
from FindImg import *

def ClickNext():
    findImgAndClick('input/Next.png')


def loginGoogle(email):
    SignInPage = findImgAndClick('input/SignInPage.png', 200, 268)
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.write(email)
    pyautogui.moveTo(SignInPage[0]-400, SignInPage[1]+268)
    pyautogui.click()
    ClickNext()


def confirmPassword():
    time.sleep(3)
    SignInPage = findImgAndClick('input/SignInPage.png', 200, 338)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.write('dplus12345')
    pyautogui.moveTo(SignInPage[0]-400, SignInPage[1]+268)
    pyautogui.click()
    ClickNext()

def saveResult(dataToSave) : 
    resultDF = pd.DataFrame(dataToSave)
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    dt_stringDir = datetime.now().strftime("%d-%m-%Y%H%M%S")
    print('finished at ',dt_string)
    resultDF.to_csv('output/'+dt_stringDir+'.csv', index=False,header=None)

dataFile = pd.read_csv('input/mail.csv',header=None,names=['colA'])
result = []
countDown()
try:
    index = 1
    time.sleep(5)
    for data in dataFile['colA'] :
        lenght = dataFile['colA'].count()
        msg = 'progressing' + str(index) + '/'+ str(lenght) + ' email : ' + data
        print(msg)

        #travel to website
        time.sleep(2)
        pyautogui.hotkey('ctrl','t')
        time.sleep(1)
        pyautogui.write('takeout.google.com')
        time.sleep(1)
        pyautogui.hotkey('enter')
        findImgAndClick('input/Login.png', 150)
        findImgAndClick('input/AddAnotherAccount.png')
        time.sleep(1)

        #Login
        loginGoogle(data) 
        confirmPassword()
        time.sleep(1)

        findImgOnScreen('input/GoogleTakeOut.png')
        time.sleep(3)    
        pyautogui.hotkey('End')
        time.sleep(1)

        findImgAndClick('input/NextStep.png')
        time.sleep(2)
        pyautogui.hotkey('End')

        findImgAndClick('input/CreateExport.png')

        countDown()
        findImgAndClick('input/CurrentDownload.png')
        #ManageExport = pyautogui.locateOnScreen('input/ManageExport.png', confidence=0.9)
        #if ManageExport is None :
        #    confirmPassword()

        result.append(data)
        index = index + 1

except Exception as e:
    print(e)
finally:
    saveResult(result)
    input('press any key to close...')
