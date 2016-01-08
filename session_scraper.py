import dryscrape
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger("linkedin")
hdlr = logging.FileHandler('/tmp/linkedin.log')
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

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


boxes =['background-summary-container','background-experience-container',
        'background-languages-container', 'background-skills-container',
       'background-education-container','background-honors-container']

def pull_profile(url):
    try:
        session.visit(url)
    except:
        logger.info("ERROR! Access denied.")
        return None, None
    content = ""
    name_div = session.at_xpath('//span[@class="full-name"]')
    if not name_div:
        logger.info("ERROR! Maybe restart?")
        return None, None
    else:
        name = name_div.text()
    for b in boxes:
        try:
            divs = session.at_xpath('//div[@id="%s"]' % b)  
            for d in divs.xpath('//div[@id="%s"]/div' % b):
                content += d.text() + " "
        except:
            continue
    return content, name
