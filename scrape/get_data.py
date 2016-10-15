# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:08:20 2016

@author: Alex
"""

from lxml import html
from urllib.request import urlopen
import codecs
from bs4 import BeautifulSoup
import csv

file = codecs.open('output.html', 'r')

soup = BeautifulSoup(file)
soup.prettify()

cities = []

for table in soup.find_all("td", { "class" : 'fteam'}): 
    for cityname in table.find_all('a'):
        print(cityname.string)
        


