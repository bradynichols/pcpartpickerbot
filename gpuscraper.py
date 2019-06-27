import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from selenium import webdriver
from time import sleep

#launch url
url = "https://pcpartpicker.com/products/video-card/"

# create a new Firefox session
browser = webdriver.Firefox()
print("Connected")

browser.get(url)
sleep(2)

innerHTML = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

soup = BeautifulSoup(innerHTML, 'html.parser')

all = soup.find_all("tr", {"class":"tr__product"})

oldnames = []
for item in all:
    oldnames.append(item.find("div", {"class": "td__nameWrapper"}).text)

gpunames = []
for name in oldnames:
    spl = name.split()
    del spl[-1]
    gpunames.append(' '.join(spl))

chipsets = []
for item in all:
    chipsets.append(item.find("td", {"class": "td__spec td__spec--1"}).text[7:])

memories = []
for item in all:
    memories.append(item.find("td", {"class": "td__spec td__spec--2"}).text[6:])

coreclocks = []
for item in all:
    try:
        coreclocks.append(item.find("td", {"class": "td__spec td__spec--3"}).text[10:])
    except AttributeError:
        coreclocks.append("Not Listed")

boostclocks = []
for item in all:
    try:
        boostclocks.append(item.find("td", {"class": "td__spec td__spec--4"}).text[11:])
    except AttributeError:
        boostclocks.append("Not Listed")

interfaces = []
for item in all:
    interfaces.append(item.find("td", {"class": "td__spec td__spec--5"}).text[9:])

colors = []
for item in all:
    try:
        colors.append(item.find("td", {"class": "td__spec td__spec--6"}).text[5:])
    except AttributeError:
        colors.append("Not Listed")

gpuprices = []
for item in all:
    gpuprices.append(item.find("td", {"class": "td__price"}).text[:-3])

data = {'Name': gpunames,
        'Price': gpuprices,
        'Chipset': chipsets,
        'Memory': memories,
        'Core Clock': coreclocks,
        'Boost Clock': boostclocks,
        'Interface': interfaces,
        'Colors': colors, }

GPUDF1 = pd.DataFrame(data)
GPUDF = GPUDF1.set_index("Name", drop=True)