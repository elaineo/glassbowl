from bs4 import BeautifulSoup
import requests

def publish_profiles(dict):
    url = "http://www.linkedin.com/title/"+ dict["Title"]+ " at " + dict["Company"]
    r = requests.get(url)
    profiles = BeautifulSoup(r.content).findAll('li',{'class': 'item-container'})
    stuff = []
    for p in profiles[:3]:
        href = p.find('a').fetch()['href']
        print href
        img = p.find('img')['src']
        print img
        headline = p.find('p', {'class': 'headline'})
        stuff.append({'url': href, 'img': img, 'headline': headline})
    #divs = BeautifulSoup(r.content).find('div', {'id': b})
    return stuff