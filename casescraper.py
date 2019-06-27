import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from selenium import webdriver
from time import sleep

#launch url
url = "https://pcpartpicker.com/products/case/"

# create a new Firefox session
browser = webdriver.Firefox()
print("Connected")

browser.get(url)
sleep(2)

innerHTML = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

soup=BeautifulSoup(innerHTML, 'html.parser')

all = soup.find_all("tr", {"class":"tr__product"})

types = []
colors = []
windows = []
extbays = []
intbays = []
caseprices = []
oldnames = []
casenames = []

for item in all:
    oldnames.append(item.find("div", {"class":"td__nameWrapper"}).text)
    types.append(item.find("td", {"class":"td__spec td__spec--1"}).text[4:])
    colors.append(item.find("td", {"class":"td__spec td__spec--2"}).text[5:])
    windows.append(item.find("td", {"class":"td__spec td__spec--4"}).text[17:])
    extbays.append(item.find("td", {"class":"td__spec td__spec--5"}).text[19:])
    intbays.append(item.find("td", {"class":"td__spec td__spec--6"}).text[18:])
    caseprices.append(item.find("td", {"class":"td__price"}).text[:-3])
for name in oldnames:
    spl = name.split()
    del spl[-1:]
    casenames.append(' '.join(spl))

data = {'Name':casenames,
        'Price':caseprices,
        'Type':types,
        'Color':colors,
        'Window?':windows,
        'External 5.25" Bays':extbays,
        'Internal 3.5" Bays':intbays}

CASEDF1 = pd.DataFrame(data)
CASEDF = CASEDF1.set_index("Name", drop = True)