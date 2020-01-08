from time import sleep
from pyautogui import hotkey
import pyautogui
import os


def enter_website(website):
    for letter in website:
        hotkey(letter)
        sleep(0.03)


curr_file = os.getcwd()
restart_btn = os.path.join(curr_file, 'Tor_location/restart_old.png')

loc = pyautogui.locateCenterOnScreen(restart_btn)
x = pyautogui.click(loc)
# Enter website
hotkey('ctrl', 'l')
enter_website('https://www.iplocation.net/')
hotkey('enter')

"""
for i in range(200):
    print(i)
    # Refresh Tor
    try:
        loc = pyautogui.locateCenterOnScreen(
            f'/home/alex/Documents/calculator/restart_old.png')
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
"""
