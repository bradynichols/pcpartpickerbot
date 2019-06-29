import requests
from bs4 import BeautifulSoup
from selenium import webdriver #Selenium is only needed in this file. If the .txt files exist, selenium is no longer needed
from time import sleep #Needed to ensure that webpages load

#BUILD DATA
r = requests.get("https://pcpartpicker.com/guide/")
c = r.content
soup = BeautifulSoup(c, "html.parser")
with open(r'.\storeddata\buildsdata.txt', 'w+') as f:
    f.write("%s\n" % soup)
    f.close()

#CPU DATA
url = "https://pcpartpicker.com/products/cpu/"
browser = webdriver.Firefox()
browser.get(url)
sleep(2)
innerHTML = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(innerHTML, 'html.parser')
with open(r'.\storeddata\cpudata.txt', 'w+') as f:
    f.write("%s\n" % soup)
    f.close()

#GPU DATA
r = requests.get("https://www.techpowerup.com/gpu-specs/")
c = r.content
soup = BeautifulSoup(c, "html.parser")
with open(r'.\storeddata\gpudata.txt', 'w+') as f:
    f.write("%s\n" % soup)
    f.close()

#MOTHERBOARD DATA
url = "https://pcpartpicker.com/products/motherboard/"
browser = webdriver.Firefox()
browser.get(url)
sleep(2)
innerHTML = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(innerHTML, 'html.parser')
with open(r'.\storeddata\mboarddata.txt', 'w+') as f:
    f.write("%s\n" % soup)
    f.close()

#CASE DATA
url = "https://pcpartpicker.com/products/case/"
browser = webdriver.Firefox()
browser.get(url)
sleep(2)
innerHTML = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(innerHTML, 'html.parser')
with open(r'.\storeddata\casedata.txt', 'w+') as f:
    f.write("%s\n" % soup)
    f.close()
