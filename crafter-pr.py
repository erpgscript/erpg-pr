
# Be sure to keep an eye on ur discord every now and then
# just try to not get into jail xdd

# crafts in batches of 1000 epic logs

# to stop the script, hover mouse to top left corner of your screen

import pyautogui as pag
import time
import random

pag.FAILSAFE = True

while True:
    time.sleep(1.5)
    pag.write('rpg craft epic log 1000')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))
    pag.write('rpg dismantle epic log all')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))