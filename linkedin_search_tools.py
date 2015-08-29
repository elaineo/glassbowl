from bs4 import BeautifulSoup
import requests

def publish_profiles(dict):
    url = "http://www.linkedin.com/title/"+ dict["Title"]+ " at " + dict["Company"]
    r = requests.get(url)
    return rank
print publish_profiles({"Company":"Oracle", "Title":"Senior Sales Executive"})


