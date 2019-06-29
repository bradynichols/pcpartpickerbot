from bs4 import BeautifulSoup
import pandas as pd

with open(r'.\storeddata\buildsdata.txt', 'r') as f:
    text = f.read()
data = BeautifulSoup(text, "html.parser")
all = data.find_all("li", {"class": "guideGroup guideGroup__card"})

names = []
prices = []

def round_nearest(x, num=50):
    return int(round(float(x) / num) * num)

for item in all:
    names.append(item.find("h1", {"class": "guide__title"}).text.replace("\n", "").strip())
    prices.append(item.find("p", {"class": "guide__price"}).text.replace("\n", "").strip())

rounded_prices = []
for price in prices:
    rounded_prices.append("$" + str(round_nearest(price[1:])))

builds_string = ""
for name, price in zip(names, rounded_prices):
    builds_string = builds_string + "\n" + name + " | **" + price + "**"


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

oldlinks = []
for item in all:
    oldlink = item.find_all("a", {"class":"guideGroup__target"})
    oldlinks.append(str(oldlink))
links = []
for item in oldlinks:
    soupyeet = BeautifulSoup(item, "html.parser")
    links.append(soupyeet.find("a").get("href"))
newlinks = []
for link in links:
    newlinks.append("https://pcpartpicker.com" + str(link))

lowernames = []
for name in names:
    lowernames.append(name.lower())

data = {'Name':lowernames,
        'Price':rounded_prices,
        'CPU':cpus,
        'GPU':gpus,
        'Case':cases,
        'Link':newlinks}


BUILDDF1 = pd.DataFrame(data)
BUILDDF = BUILDDF1.set_index("Name", drop = True)
