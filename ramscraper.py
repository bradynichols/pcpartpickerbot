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
for item in all:
    oldnames.append(item.find("div", {"class": "td__nameWrapper"}).text)

ramnames = []
for name in oldnames:
    spl = name.split()
    del spl[-3:]
    ramnames.append(' '.join(spl))

speeds = []
for item in all:
    speeds.append(item.find("td", {"class": "td__spec td__spec--1"}).text[5:])

types = []
for item in all:
    type = item.find("td", {"class": "td__spec td__spec--2"}).text[4:]
    if type != '288-pin DIMM':
        types.append(type)
    else:
        types.append("")

moduleslist = []
for item in all:
    moduleslist.append(item.find("td", {"class": "td__spec td__spec--3"}).text[7:])

pricepergigs = []
for item in all:
    try:
        pricepergigs.append(item.find("td", {"class": "td__spec td__spec--4"}).text[10:])
    except:
        pricepergigs.append("Not Listed")

caslats = []
for item in all:
    caslats.append(item.find("td", {"class": "td__spec td__spec--6"}).text[11:])

ramprices = []
for item in all:
    ramprices.append(item.find("td", {"class": "td__price"}).text[:-3])

data = {'Name': ramnames,
        'Price': ramprices,
        'Speed': speeds,
        'Type': types,
        'Module': moduleslist,
        'PPG': pricepergigs,
        'CAS Latency': caslats}

RAMDF1 = pd.DataFrame(data)
RAMDF = RAMDF1.set_index("Name", drop=True)