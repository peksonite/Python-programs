import random
import time

import pyautogui as pag

while True:
    x = random.randint(600,700)
    y = random.randint(200,600)
    pag.moveTo(x,y,0.5)
    time.sleep(5)
