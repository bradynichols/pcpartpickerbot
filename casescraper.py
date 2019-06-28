from bs4 import BeautifulSoup
import pandas as pd


with open(r'.\storeddata\casedata.txt', 'r') as f:
    text = f.read()
data = BeautifulSoup(text, "html.parser")
all = data.find_all("tr", {"class":"tr__product"})

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

lowernames = []
for name in casenames:
    lowernames.append(name.lower())

data = {'Name':lowernames,
        'Price':caseprices,
        'Type':types,
        'Color':colors,
        'Window?':windows,
        'External 5.25" Bays':extbays,
        'Internal 3.5" Bays':intbays}

CASEDF1 = pd.DataFrame(data)
CASEDF = CASEDF1.set_index("Name", drop = True)
print(CASEDF)