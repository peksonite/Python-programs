import os
import shutil

import pyqrcode

title = input("Give your QR code a title! >>")
text = input("What woould you like the QR code to say? >>")

file_name__svg = title + ".svg"
file_name_png = title + ".png"

url = pyqrcode.create(text)

url.svg(file_name__svg, scale=8)
url.png(file_name_png, scale=10)

os.mkdir(fr"C:\Users\kplachta\Desktop\{title}")

shutil.move(file_name_png, fr"C:\Users\kplachta\Desktop\{title}")
shutil.move(file_name__svg, fr"C:\Users\kplachta\Desktop\{title}")
