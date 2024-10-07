## to open the frequently used websites in chrome/web browser

import webbrowser as wb

def open_web():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe ' ## path to the chrome.exe file
    URLS = {
        'google.com',
        'facebook.com',
        'github.com',
        'youtube.com'

    }

    for url in URLS:
        wb.get(chrome_path).open(url)
        wb.open(url)
    
open_web()