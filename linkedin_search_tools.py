from bs4 import BeautifulSoup
import requests

def publish_profiles(dict):
    url = "http://www.linkedin.com/title/"+ dict["Title"]+ "at" + dict["Company"]
    r = requests.get(url)
    print r.content
    rank = BeautifulSoup(r.content).find("div", {"class": "media-body"}).contents
    #divs = BeautifulSoup(r.content).find('div', {'id': b})
    return rank

print publish_profiles({"Company":"Oracle", "Title":"Senior Sales Executive"})


