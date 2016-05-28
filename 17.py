#!/usr/bin/python
## http://www.practicepython.org/
#plugin pre parsovanie html ktory dokaze precitat nazvy clankov

__author__ = 'tomas.balazsik'

import requests
from bs4 import BeautifulSoup
url = 'http://www.cas.sk/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
for heading in soup.find_all("span", { 'class' : 'xs-visible'}):
#encode je kvoli problemom s citanim textu a predavanim dalej do pipy v linuxe
 print(heading.text.encode('UTF-8').strip())
#for heading in soup.find_all("a"):
# print(heading.get('href'))
