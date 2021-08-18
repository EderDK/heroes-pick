
import time
from typing import Counter
import requests #
import pandas as pd #
from bs4 import BeautifulSoup #
from selenium import webdriver #
from selenium.webdriver.firefox.options import Options
import json
import re
from pprint import pprint

Ndict = {}
lista = [ "WarheadJunction",
         "TowersofDoom",
         "TomboftheSpiderQueen",
         "SkyTemple",
         "AlteracPass",
         "InfernalShrines",
         "BattlefieldofEternity",
         "BraxisHoldout",
         "HanamuraTemple",
         "GardenofTerror",
         "CursedHollow",
         "DragonShire"  
         
         ]

url = [
    r"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Warhead%20Junction"
    r"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Towers%20of%20Doom",
    r"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Tomb%20of%20the%20Spider%20Queen",
    r"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Sky%20Temple",
    r"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Alterac%20Pass&Patch=85311-85576,85267-85267",
    r"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Infernal%20Shrines",
    r"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Battlefield%20of%20Eternity&Patch=85311-85576,85267-85267",
    r"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Braxis%20Holdout&Patch=85311-85576,85267-85267",
    r"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Hanamura%20Temple",
    r"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Garden%20of%20Terror",
    r"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Cursed%20Hollow&Patch=85311-85576,85267-85267",
    r"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Dragon%20Shire&Patch=85311-85576,85267-85267"
]

option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)
#r = re.compile("\(.*")

for nome_Mapa, link in zip(lista,url):
    driver.get(link)
    dict = {}
    x = 0
    

    while True:
        x += 1
        try:
            pers_element = driver.find_element_by_xpath(
            '/html/body/form/div[4]/section/div[4]/div/div[3]/div[1]/table/tbody/tr['+str(x)+']/td[2]/a') # /html/body/form/div[4]/section/div[4]/div/div[3]/div[1]/table/tbody/tr[1]/td[2]/a
            personagem_name = pers_element.get_attribute('innerHTML')                           # /html/body/form/div[4]/section/div[4]/div/div[3]/div[1]/table/tbody/tr[3]/td[2]/a
            print(personagem_name)
            element = driver.find_element_by_xpath(
                '/html/body/form/div[4]/section/div[4]/div/div[3]/div[1]/table/tbody/tr['+str(x)+']/td[6]') #/html/body/form/div[4]/section/div[4]/div/div[3]/div[1]/table/tbody/tr[1]/td[6]/
            html_content = str(element.get_attribute('innerHTML'))
            html_content = html_content.split('<')[0]
            print(html_content)
            dict[x] = [personagem_name,html_content]
            
        except:
            break
    Ndict[nome_Mapa] = dict
    
pprint(Ndict,sort_dicts=False)
js = json.dumps(Ndict, indent=4, ensure_ascii=False)
fp = open('Winrate_Map.json', 'w', encoding='utf-8')
fp.write(js)
fp.close()
