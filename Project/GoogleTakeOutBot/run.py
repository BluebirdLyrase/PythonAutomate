from PIL import Image
import os
import time
import pyautogui
import pandas as pd
from datetime import datetime

def ClickNext() :
    Next = pyautogui.locateOnScreen('input/Next.png', confidence=0.9)
    while Next is None :
        print('cannot find Next Button')
        time.sleep(1)
        Next = pyautogui.locateOnScreen('input/Next.png', confidence=0.9)  
    pyautogui.moveTo(Next[0]+10, Next[1]+10)
    pyautogui.click() 

def loginGoogle(email) :
    print("Logginh in " + email)
    SignInPage = pyautogui.locateOnScreen('input/SignInPage.png', confidence=0.9)
    while SignInPage is None :
        print('cannot find SignInPage')
        time.sleep(1)
        SignInPage = pyautogui.locateOnScreen('input/SignInPage.png', confidence=0.9)  
    pyautogui.moveTo(SignInPage[0]+200, SignInPage[1]+268)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click() 
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.write(email)
    pyautogui.moveTo(SignInPage[0]-400, SignInPage[1]+268)
    pyautogui.click()
    ClickNext()

    
def confirmPassword() :
    time.sleep(3)
    SignInPage = pyautogui.locateOnScreen('input/SignInPage.png', confidence=0.9)
    while SignInPage is None :
        print('cannot find SignInPage')
        time.sleep(1)
        SignInPage = pyautogui.locateOnScreen('input/SignInPage.png', confidence=0.9)  
    pyautogui.moveTo(SignInPage[0]+200, SignInPage[1]+338)
    pyautogui.click() 
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
try:
    index = 1
    for data in dataFile['colA'] :
        lenght = dataFile['colA'].count()
        msg = 'progressing' + str(index) + '/'+ str(lenght) + ' email : ' + data
        print(msg)

        time.sleep(2)
        pyautogui.hotkey('ctrl','t')
        time.sleep(1)
        pyautogui.write('takeout.google.com')
        time.sleep(1)
        pyautogui.hotkey('enter')

        Login = pyautogui.locateOnScreen('input/Login.png', confidence=0.9)
        while Login is None :
            print('cannot find Login')
            time.sleep(1)
            Login = pyautogui.locateOnScreen('input/Login.png', confidence=0.9) 
        pyautogui.moveTo(Login[0]+150, Login[1]+10)
        pyautogui.click()

        AddAnotherAccount = pyautogui.locateOnScreen('input/AddAnotherAccount.png', confidence=0.9)
        while AddAnotherAccount is None :
            print('cannot find AddAnotherAccount')
            time.sleep(1)
            AddAnotherAccount = pyautogui.locateOnScreen('input/AddAnotherAccount.png', confidence=0.9) 
        pyautogui.moveTo(AddAnotherAccount[0]+10, AddAnotherAccount[1]+10)
        pyautogui.click()
        time.sleep(1)

        loginGoogle(data) 
        confirmPassword()
        time.sleep(1)

        GoogleTakeOut = pyautogui.locateOnScreen('input/GoogleTakeOut.png', confidence=0.9)
        while GoogleTakeOut is None :
            print('cannot find GoogleTakeOut')
            time.sleep(1)
            GoogleTakeOut = pyautogui.locateOnScreen('input/GoogleTakeOut.png', confidence=0.9)  
        time.sleep(3)    
        pyautogui.hotkey('End')
        time.sleep(1)

        NextStep = pyautogui.locateOnScreen('input/NextStep.png', confidence=0.9)
        while NextStep is None :
            print('cannot find NextStep')
            time.sleep(1)
            NextStep = pyautogui.locateOnScreen('input/NextStep.png', confidence=0.9)  
        pyautogui.moveTo(NextStep[0]+10, NextStep[1]+10)
        pyautogui.click()
        time.sleep(2)
        pyautogui.hotkey('End')

        CreateExport = pyautogui.locateOnScreen('input/CreateExport.png', confidence=0.9)
        while CreateExport is None :
            print('cannot find CreateExport')
            time.sleep(1)
            CreateExport = pyautogui.locateOnScreen('input/CreateExport.png', confidence=0.9)  
        pyautogui.moveTo(CreateExport[0]+10, CreateExport[1]+10)
        pyautogui.click()
        time.sleep(1)

        CurrentDownload = pyautogui.locateOnScreen('input/CurrentDownload.png', confidence=0.9)
        while CurrentDownload is None :
            print('cannot find CurrentDownload')
            time.sleep(1)
            CurrentDownload = pyautogui.locateOnScreen('input/CurrentDownload.png', confidence=0.9)  
        pyautogui.moveTo(CurrentDownload[0]+10, CurrentDownload[1]+10)
        pyautogui.click()

        time.sleep(5)
        ManageExport = pyautogui.locateOnScreen('input/ManageExport.png', confidence=0.9)
        if ManageExport is None :
            confirmPassword()

        result.append(data)
        index = index + 1
        time.sleep(5)
    
    saveResult(result)
except Exception as e:
    saveResult(result)
    print("Error")
    print(e)
except KeyboardInterrupt:
    saveResult(result)