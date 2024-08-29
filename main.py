import pyautogui as pyt
import time

message = "Shodi v magaz pls"
count = 400
i = 0

time.sleep(5) 

while i < int(count):
    pyt.typewrite(message)
    pyt.press("enter")
    i+=1