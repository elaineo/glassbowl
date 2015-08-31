from bs4 import BeautifulSoup
import requests

def publish_profiles(dict):
    url = "http://www.linkedin.com/title/"+ dict["Title"]+ " at " + dict["Company"]
    r = requests.get(url)
    profiles = BeautifulSoup(r.content).findAll('li',{'class': 'item-container'})
    stuff = []
    for p in profiles:
        href = p.find('a').fetch()['href']
        img = p.find('img')['src']
        headline = p.find('p', {'class': 'headline'}).getText()
        stuff.append({'url': href, 'img': img, 'headline': headline})
    #divs = BeautifulSoup(r.content).find('div', {'id': b})
    return stuff[:3]