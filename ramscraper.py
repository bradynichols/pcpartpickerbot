import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from selenium import webdriver
from time import sleep

# launch url
url = "https://pcpartpicker.com/products/memory/"

# create a new Firefox session
browser = webdriver.Firefox()
print("Connected")

browser.get(url)
sleep(2)

innerHTML = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

soup = BeautifulSoup(innerHTML, 'html.parser')

all = soup.find_all("tr", {"class": "tr__product"})

oldnames = []
ramprices = []
caslats = []
pricepergigs = []
moduleslist = []
types = []
speeds = []

for item in all:
    speeds.append(item.find("td", {"class": "td__spec td__spec--1"}).text[5:])
    typee = item.find("td", {"class": "td__spec td__spec--2"}).text[4:]

    if typee != '288-pin DIMM':
        types.append(typee)
    else:
        types.append("")

    moduleslist.append(item.find("td", {"class": "td__spec td__spec--3"}).text[7:])

    try:
        pricepergigs.append(item.find("td", {"class": "td__spec td__spec--4"}).text[10:])
    except:
        pricepergigs.append("Not Listed")

    caslats.append(item.find("td", {"class": "td__spec td__spec--6"}).text[11:])
    ramprices.append(item.find("td", {"class": "td__price"}).text[:-3])
    oldnames.append(item.find("div", {"class": "td__nameWrapper"}).text)

ramnames = []
for name in oldnames:
    spl = name.split()
    del spl[-1:]
    ramnames.append(' '.join(spl))

data = {'Name': ramnames,
        'Price': ramprices,
        'Speed': speeds,
        'Type': types,
        'Module': moduleslist,
        'PPG': pricepergigs,
        'CAS Latency': caslats}

RAMDF1 = pd.DataFrame(data)

indicestoremove = []
for x in ramnames:
    ppg = RAMDF1.loc[ramnames.index(x), "PPG"]
    if ppg == "Not Listed":
        print(x)
        indicestoremove.append(ramnames.index(x))

for i in reversed(indicestoremove):
    RAMDF1 = RAMDF1.drop([i], axis=0)

RAMDF = RAMDF1.set_index("Name", drop=True)