import dryscrape
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger("linkedin")
hdlr = logging.FileHandler('/tmp/linkedin.log')
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)




boxes =['background-summary-container','background-experience-container',
        'background-languages-container', 'background-skills-container',
       'background-education-container','background-honors-container']

def pull_profile(url):
    dryscrape.start_xvfb()
    session = dryscrape.Session()
    # Get George set up
    session.visit("https://www.linkedin.com")
    # log in
    q = session.at_xpath('//*[@id="login-email"]')
    q.set('george@sandhill.exchange')
    q = session.at_xpath('//*[@id="login-password"]')
    q.set("GlassBowl")
    button = session.at_xpath('//*[@name="submit"]')
    button.click()
    session.visit(url)
    content = ""
    for b in boxes:
        try:
            divs = session.at_xpath('//div[@id="%s"]' % b)  
            for d in divs.xpath('//div[@id="%s"]/div' % b):
                content += d.text() + " "
        except:
            continue
    return content
