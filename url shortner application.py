
import pyshorteners

url = input("Enter URL for Shortening : \n")

print("URL after shortening :- ",pyshorteners.Shortener().tinyurl.short(url))

