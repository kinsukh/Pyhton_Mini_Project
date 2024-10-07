## requirments = pyshorteners

import pyshorteners

url = input("Enter the URL: ")

shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(url)

print("Short URL: ", short_url)