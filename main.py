#!/usr/bin/python3
# create : males lanjutin

import requests
import time
from bs4 import BeautifulSoup
from rich import print
from rich.table import Table
from rich.panel import Panel
import os,sys

# clear_display
clr = lambda : os.system('clear')

class Main:
    def __init__(self):
        ''' pass '''
        self.url = "https://whatmyuseragent.com/engines"
        self.web = "/Webkit"
        self.blink = "/Blink"
        self.trident = "/Trident"
        self.text_based = "/Text-based" 
        self.khtml = "/KHTML"
        self.gecko = "/Gecko"
        self.number = 0
        self.features = "html.parser"

    def _gecko_(self):
        clr()
        url = self.url + self.gecko
        req = requests.get(url)
        so = BeautifulSoup(req.text,features=self.features)
#        lsd = ['href']
#        for lsd in so.find_all('a',href=True):
        for c in so.find_all('td',class_="useragent"):
            self.number += 1
            print(Panel(f"{c.text}",title=f"[ {self.number} ]",title_align="left"))
   
    def _blink_(self):
        clr()
        url = self.url + self.blink
        req = requests.get(url)
        so = BeautifulSoup(req.text,features=self.features)
        for c in so.find_all('td',class_="useragent"):
            self.number += 1
            print(Panel(f"{c.text}",title=f"[ {self.number} ]",title_align="left"))

    def _webkit_(self):
        clr()
        url = self.url + self.web
        req = requests.get(url)
        so = BeautifulSoup(req.text,features=self.features)
        for c in so.find_all('td',class_="useragent"):
            self.number += 1
            print(Panel(f"{c.text}",title=f"[ {self.number} ]",title_align="left"))

    def _engine_(self):
        url = self.url
        req = requests.get(url)
        so = BeautifulSoup(req.text,features=self.features)
        for c in so.find_all('li')[1:15]:
            print(c.text)

