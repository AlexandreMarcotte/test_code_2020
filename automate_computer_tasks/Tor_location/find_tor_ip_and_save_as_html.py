from time import sleep
from pyautogui import hotkey
import pyautogui
from bs4 import BeautifulSoup as soup


def open_tor_browser():
    sleep(0.5)
    hotkey('winleft')
    sleep(1)
    pyautogui.typewrite('tor')
    hotkey('enter')
    sleep(2)


def enter_website():
    sleep(0.1)
    hotkey('ctrl', 'l')
    sleep(0.1)
    pyautogui.typewrite('https://www.iplocation.net/', interval=0.01)
    hotkey('enter')
    sleep(7)


def wait_till_website_loaded():
    # Wait till the website is loaded
    on_ip_location_website = False
    # Wait till we see the logo of the website which means that the website is loaded
    while not on_ip_location_website:
        sleep(1)
        on_ip_location_website = pyautogui.locateCenterOnScreen(
                'ip_location_logo.png')


def restart_tor_session():
    sleep(1)
    loc = pyautogui.locateCenterOnScreen('restart_btn.png')
    pyautogui.click(loc)
    sleep(2)


def save_html():
    hotkey('ctrl', 's')
    # To go in the save box
    hotkey('enter')
    # To replace the existing file
    sleep(3)
    hotkey('enter')
    # Wait for it to save
    sleep(7)




def pull_html_from_ip_adress_site_on_tor():
    # on first pass only
    open_tor_browser()
    restart_tor_session()
    enter_website()
    save_html()


if __name__ == '__main__':
    # Test
    pull_html_from_ip_adress_site_on_tor()

