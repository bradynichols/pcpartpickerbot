import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

r = requests.get("https://pcpartpicker.com/guide/")
c = r.content

soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("li", {"class": "guideGroup guideGroup__card"})

names = []
prices = []

for item in all:
    names.append(item.find("h1", {"class": "guide__title"}).text.replace("\n", "").strip())
    prices.append(item.find("p", {"class": "guide__price"}).text.replace("\n", "").strip())

dict = {}

for name, price in zip(names, prices):
    dict.update({name: price})

components1 = []
cpus = []
for item in all:
    components1.append(str(item.find_all("ul", {"class": "guide__keyProducts list-unstyled"})))
alls = []
for item in components1:
    soupyeet = BeautifulSoup(item, "html.parser")
    alls.append(soupyeet.find_all("li"))

oldcpus = []
oldgpus = []
oldcases = []

for x in range(0, 1000):
    try:
        oldcpus.append(alls[x][0])
        try:
            oldcases.append(alls[x][2])
            oldgpus.append(alls[x][1])
        except:
            oldgpus.append("No GPU")
            oldcases.append(alls[x][1])

    except:
        break

cpus = []
gpus = []
cases = []
for cpu, gpu, case in zip(oldcpus, oldgpus, oldcases):
    cpus.append(str(cpu).replace("<li>", "").replace("</li>", ""))
    gpus.append(str(gpu).replace("<li>", "").replace("</li>", ""))
    cases.append(str(case).replace("<li>", "").replace("</li>", ""))

data = {'Name': names,
        'Price': prices,
        'CPU': cpus,
        'GPU': gpus,
        'Case': cases}


BUILDDF1 = pd.DataFrame(data)
BUILDDF = BUILDDF1.set_index("Name", drop = True)

#IDEA: SELECT BUILDS USING [1] TO [9] OR WHATEVER
columntitles = list(BUILDDF.columns.values)
imput = "Great AMD Gaming/Streaming Build"
cpue = BUILDDF.loc[input, "CPU"]
gpue = BUILDDF.loc[input, "GPU"]
casee = BUILDDF.loc[input, "Case"]
print(cpue)
print(gpue)
print(casee)