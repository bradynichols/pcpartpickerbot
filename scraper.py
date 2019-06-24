import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://pcpartpicker.com/guide/")
c = r.content

soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("li", {"class":"guideGroup guideGroup__card"})

names = []
prices = []

for item in all:
    names.append(item.find("h1", {"class": "guide__title"}).text.replace("\n", "").strip())
    prices.append(item.find("p", {"class": "guide__price"}).text.replace("\n", "").strip())


dict = {}
builds_string = ""

for name, price in zip(names, prices):
    dict.update({name: price})
    builds_string = builds_string + "**" + name + "**: " + price + " | "

print(dict)
print(builds_string)