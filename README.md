# Discord-QR-Scam
Discord Image Token Grabber 

### About
A Python script that automatically generates a Nitro scam QR code and grabs the Discord token when scanned. This tool demonstrates how people can trick others
into scanning their Discord login QR Code, and gain access to their account. Use for Educational Purposes only.

![img1](https://i.ibb.co/BL2Q0jz/Screenshot-527.png)

## Demonstration
![qr-code](https://user-images.githubusercontent.com/75003671/117522092-fd79ff80-afe3-11eb-938c-23dd68d5927c.gif)

## Info
Download the latest version of [chromedriver](https://chromedriver.chromium.org/downloads), and replace the old chromedriver.exe with the new one.  If you get any errors, scroll down to troubleshoot to learn more.

## Usage
1. If you dont have python installed, download python 3.7.6
and make sure you click on the 'ADD TO PATH' option during
the installation.

2. Install the required modules > ```pip install -r requirements.txt``` or double click `pip_install_requirements.bat`

3. Type ```python QR_Generator.py``` in cmd to run or double click `run_script.bat`

4. Wait for the `discord_gift.png` to be generated. Send the image to the victim and make them scan it.

5. QR Code only lasts about 2 minutes. Make sure you send a fresh one to the victim and he is ready to scan.

6. When the QR Code is scanned, you will automatically be logged in to their account and the script will grab the Discord token.

## Troubleshoot
Make sure your chromedriver.exe file is the same version as your current Chrome web browser version. To check your current Chrome version,
paste `chrome://settings/help` in Google Chrome.

if Chrome crashes,

1. Make sure your chromedriver.exe file is the same version as your Chrome web browser version
2. Download the latest version chromedriver.exe here: https://chromedriver.chromium.org/downloads
3. Then replace the chromedriver.exe file in the folder.

