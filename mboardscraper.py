import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from selenium import webdriver
from time import sleep

#launch url
url = "https://pcpartpicker.com/products/motherboard/"

# create a new Firefox session
browser = webdriver.Firefox()
print("Connected")

browser.get(url)
sleep(2)

innerHTML = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

soup=BeautifulSoup(innerHTML, 'html.parser')

all = soup.find_all("tr", {"class":"tr__product"})
oldnames = []
mbnames = []
sockets = []
formfactors = []
ramslots = []
maxram = []
colors = []
mbprices = []

for item in all:
    oldnames.append(item.find("div", {"class": "td__nameWrapper"}).text)
    sockets.append(item.find("td", {"class": "td__spec td__spec--1"}).text[12:])
    formfactors.append(item.find("td", {"class": "td__spec td__spec--2"}).text[11:])
    ramslots.append(item.find("td", {"class": "td__spec td__spec--3"}).text[9:])
    maxram.append(item.find("td", {"class": "td__spec td__spec--4"}).text[7:])
    colors.append(item.find("td", {"class": "td__spec td__spec--5"}).text[5:])
    mbprices.append(item.find("td", {"class": "td__price"}).text[:-3])

for name in oldnames:
    spl = name.split()
    del spl[-1]
    mbnames.append(' '.join(spl))

data = {'Name': mbnames,
        'Price': mbprices,
        'Sockets': sockets,
        'Form Factor': formfactors,
        'RAM Slots': ramslots,
        'Max RAM': maxram,
        'Colors': colors}

MBOARDDF1 = pd.DataFrame(data)
MBOARDDF = MBOARDDF1.set_index("Name", drop=True)