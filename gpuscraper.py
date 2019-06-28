import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

r = requests.get("https://www.techpowerup.com/gpu-specs/")
c = r.content

soup = BeautifulSoup(c, "html.parser")

ball = soup.find("table", {"class": "processors"})
all = ball.find_all("tr")

tds = []
for item in all:
    tds.append(item.find_all("td"))
del tds[0:2]

names = []
chips = []
releases = []
busses = []
memories = []
gpuclocks = []
memclocks = []
strlist = []
for item in tds:
    itemyeet = BeautifulSoup(str(item), "html.parser")
    names.append(itemyeet.find("a").text)
    chips.append(itemyeet.find_all("td")[1].text.replace("\n", ""))
    releases.append(itemyeet.find_all("td")[2].text.replace("\n", ""))
    busses.append(itemyeet.find_all("td")[3].text.replace("\n", ""))
    memories.append(itemyeet.find_all("td")[4].text.replace("\n", ""))
    gpuclocks.append(itemyeet.find_all("td")[5].text.replace("\n", ""))
    memclocks.append(itemyeet.find_all("td")[6].text.replace("\n", ""))
    strlist.append(itemyeet.find_all("td")[7].text.replace("\n", ""))

lowernames = []
for name in names:
    lowernames.append(name.lower())

data = {'Name': lowernames,
        'Chip': chips,
        'Release': releases,
        'Bus': busses,
        'Memory': memories,
        'GPU Clock': gpuclocks,
        'Memory Clock': memclocks,
        'Shaders / TMUs / ROPs': strlist}

GPUDF1 = pd.DataFrame(data)
GPUDF = GPUDF1.set_index("Name", drop=True)