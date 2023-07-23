import pyautogui
import time
time.sleep(4);
count=0
while count <=30:
    pyautogui.typewrite("Tor bou jutbe na   "+str(count))
    pyautogui.press("enter")
    count=count+1
``

