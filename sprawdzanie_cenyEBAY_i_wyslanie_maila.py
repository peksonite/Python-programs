#https://www.youtube.com/watch?v=Qb8pM83POTw

import smtplib
import ssl
import sys
import time

import requests
from lxml import html

# URL = 'https://ebay.com/'
URL = 'https://www.ebay.pl/itm/303811343016?hash=item46bc9132a8%3Ag%3AD7YAAOSw9rJedj%7EZ&_trkparms=%2526rpp_cid%253D6262871bb17babf6819a6da9'

headers = {"User-Agent": 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers=headers)
    tree = html.fromstring(page.content)

    buyers = str(tree.xpath('//h1[@class="it-ttl"]/text()'))
    for t in (("[", ""), ("]", ""), ("'", ""), (",", ""), ("\\n", ""), ("\\t", "")):
        buyers = buyers.replace(*t)

        prices = str(tree.xpath('//span[@class="notranslate"]/text()'))
        for r in (("GBP", ""), (" EUR", ""), ("[", ""), ("]", ""), ("'", ""), ("US $", ""), (",", "")):
            prices = prices.replace(*r)

        convert_prices = float(prices[0:100])

        if (convert_prices < 100):
            send_email()
            value = str(convert_prices)
            print('Good price '+ value)
        else:
            value = str(convert_prices)
            print('Bad price '+ value)
            y = 5
            howtime = y*60
            time.sleep(howtime)
            check_price()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("pekson.production@gmail.com", "kochampacke1")

    subject = "Go to ebay Now!!!"
    body = "Check the item link " + URL + " the price is below 100"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'pekson.production@gmail.com',
        'k.plachta@hotmail.com',
        msg)

    print("Mail sent")

    server.quit()

check_price()
