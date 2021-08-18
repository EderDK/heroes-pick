import requests #
import pandas as pd #
from bs4 import BeautifulSoup #
from selenium import webdriver #
from selenium.webdriver.firefox.options import Options
import json
import re
from pprint import pprint

heroes_tags_dic = {}
tags_dic = {}

url_geral = "https://www.heroescounters.com"

url_heroes = []
option = Options()
#option.headless = True
driver = webdriver.Firefox(options=option)

r = re.compile('href=".*" t')
driver.get(url_geral)
                

for x in range(1,10):
#for x in range(1,2):
    for y in range(1,12):
#    for y in range(1,2):
        try:
            content = driver.find_element_by_xpath(
                    '/html/body/div/div[2]/div[3]/div['+str(x)+']/a['+str(y)+']'
                )
            hero_link = re.findall(r, content.get_attribute('outerHTML'))[0].split("\"")[1]
            url_heroes.append(hero_link)
        except:
            pass


for i in url_heroes:
    driver.get(url_geral+i)
    c = 1
    aux = []
    hero = i.split('/')[2]
    heroes_tags_dic[hero] = []
    while True:
        try:
        #if True:
            a = '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[1]'
            content = driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li['+str(c)+']/span')

            
            aux = heroes_tags_dic[hero]
            tag = content.get_attribute('innerHTML')
            aux.append(tag)

            if tag in tags_dic.keys():
                tags_dic[tag] += 1 
            else:
                tags_dic[tag] = 1
                
            c += 1
        
        except:
        #else:
            break
            
            
    
pprint(heroes_tags_dic)
pprint(tags_dic)

js = json.dumps(heroes_tags_dic, indent=4, ensure_ascii=False)
fp = open('heroes_tags.json', 'w', encoding='utf-8')
fp.write(js)
fp.close()

js = json.dumps(tags_dic, indent=4, ensure_ascii=False)
fp = open('tags.json', 'w', encoding='utf-8')
fp.write(js)
fp.close()


driver.quit()


