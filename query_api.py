# import MySQLdb as db
from query_tools import *
import requests
import os
import json
from minidb import getSalary
from bs4 import BeautifulSoup
import locale
locale.setlocale(locale.LC_ALL, 'en_US')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_DATA = os.path.join(APP_ROOT, 'data')

def open_file(name):
    with open(os.path.join(APP_DATA, name)) as f:
        f.read()

def search_query(url):
    data = pull_profile(url)
    documents, dictionary, lsi, index = load_docs('linkedin')

    sims = query_docs(data, dictionary, lsi, index)

    #get 10 best matches
    idx = [sims[s][0] for s in range(0,10)]

    results = index_lookup(idx)
    rtokens = [r.split('/') for r in results]
    #results = pull_linkedidx(idx)

    clean_res = [{'Company':r[2],'Title':r[3].split('.')[0]} for r in rtokens]
    jobs = getSalary(clean_res)
    min_sal, max_sal, avg_sal = calc_salary([r['Salary'] for r in jobs])
    results = {}
    results['jobs'] = jobs
    results['max_salary'] = '$' + locale.format("%d", max_sal, grouping=True) 
    results['min_salary'] = '$' + locale.format("%d", min_sal, grouping=True) 
    results['ave_salary'] = '$' + locale.format("%d", avg_sal, grouping=True) 
    return results

def calc_salary(salarylist):
    total = len(salarylist)
    numlist = []
    for s in salarylist:
        num = s.replace('$','')
        num = num.replace('k', '000')
        numlist.append(int(num))
    min_sal = min(numlist)
    max_sal = max(numlist)
    avg_sal = sum(numlist)/total
    return min_sal, max_sal, avg_sal

def index_lookup(indices):
    name = 'linkedin'

    with open(os.path.join(APP_ROOT, '%s-realidx.json' % name), 'r') as f:
        realidx = json.load(f)
    
    with open(os.path.join(APP_ROOT, '%s-files.json' % name), 'r') as f:
        filelist = json.load(f)

    r = [filelist[realidx[i]] for i in indices]
    return r

def pull_linkedidx(indices):
    conn = db.connect('localhost', 'root', '', 'mydata')
    with conn:
        cur = conn.cursor()
        results = []
        for idx in indices:
            query = "select company, title from linkedin where id = %s" % idx
            cur.execute(query)
            res = cur.fetchone()
            results.append([res[0], res[1]])
    conn.close()
    return results

boxes =['background-summary-container','background-experience-container',
        'background-languages-container', 'background-skills-container',
       'background-education-container','background-honors-container']

def pull_profile(url):
    r = requests.get(url)
    content = ""
    for b in boxes:
        try:
            divs = BeautifulSoup(r.content).find('div', {'id': b})
            for script in divs(["script", "style"]):
                script.extract()    # rip it out   
            for d in divs.findAll('div'):
                content += " ".join(d.strings) + " "
        except:
            continue
    return content