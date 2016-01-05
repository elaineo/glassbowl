import dryscrape
from bs4 import BeautifulSoup

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
    session.visit(url)
    r = session.body()
    content = ""
    for b in boxes:
        try:
            divs = session.at_xpath('//div[@id="%s"]' % b)  
            for d in divs.xpath('//div[@id="%s"]/div' % b):
                content += div.text() + " "
        except:
            continue
    return content