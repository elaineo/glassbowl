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


boxes =['summary','experience',
        'languages', 'skills',
       'education','honors']

def pull_profile(url):
    session.visit(url)
    r = session.body()
    content = ""
    for b in boxes:
        try:
            divs = BeautifulSoup(r).find('section', {'id': b})
            for script in divs(["script", "style"]):
                script.extract()    # rip it out   
            for d in divs:
                content += " ".join(d.strings) + " "
        except:
            continue
    return content