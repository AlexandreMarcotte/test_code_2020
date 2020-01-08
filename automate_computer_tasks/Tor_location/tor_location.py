from time import sleep
from pyautogui import hotkey
import pyautogui


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
        print(on_ip_location_website)


def restart_tor_session():
    sleep(1)
    loc = pyautogui.locateCenterOnScreen('restart_btn.png')
    print(loc)
    pyautogui.click(loc)
    sleep(2)


def save_html():
    hotkey('ctrl', 's')
    # To go in the save box
    hotkey('enter')
    # To replace the existing file
    sleep(2)
    hotkey('enter')
    # Wait for it to save
    sleep(3)


def open_html():
    html_path = '/home/record/.local/share/torbrowser/tbb/x86_64/tor-browser_en-US/Browser/Downloads/IP Location Finder - Geolocation.html'
    with open(html_path) as f:
        for line in f:
            print(line)


def main():
    # on first pass only
    open_tor_browser()
    restart_tor_session()
    enter_website()
    save_html()
    open_html()


if __name__ == '__main__':
    main()

