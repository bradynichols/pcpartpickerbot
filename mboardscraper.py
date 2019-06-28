from bs4 import BeautifulSoup
import pandas as pd


with open(r'.\storeddata\mboarddata.txt', 'r') as f:
    text = f.read()
data = BeautifulSoup(text, "html.parser")

all = data.find_all("tr", {"class":"tr__product"})
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

lowernames = []
for name in mbnames:
    lowernames.append(name.lower())

data = {'Name': lowernames,
        'Price': mbprices,
        'Sockets': sockets,
        'Form Factor': formfactors,
        'RAM Slots': ramslots,
        'Max RAM': maxram,
        'Colors': colors}

MBOARDDF1 = pd.DataFrame(data)
MBOARDDF = MBOARDDF1.set_index("Name", drop=True)
