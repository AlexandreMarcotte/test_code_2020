from time import sleep
from pyautogui import hotkey
import pyautogui


pyautogui.PAUSE = 0.001
site = 'https://www.bitchute.com/video/aONHInaSXlWb/'


for i in range(200):
    print(i)
    # Refresh Tor
    try:
        loc = pyautogui.locateCenterOnScreen(
            f'/home/alex/Documents/calculator/restart.png')
        pyautogui.click(loc)
    except OSError as e:
        # wait loading
        print(e)
    sleep(3)
    # Enter website
    hotkey('ctrl', 'l')
    sleep(0.5)
    for letter in site:
        hotkey(letter)
        sleep(0.03)
    sleep(1)
    hotkey('enter')
    # wait loading
    sleep(12)
