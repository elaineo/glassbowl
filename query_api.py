#import MySQLdb as db
from query_tools import *
import requests
import os
import json
from minidb import getSalary
import locale
locale.setlocale(locale.LC_ALL, 'en_US.utf8')
import logging
from session_scraper import pull_profile

logger = logging.getLogger("linkedin")
hdlr = logging.FileHandler('/tmp/linkedin.log')
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

#APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_ROOT = '/home/ubuntu'
APP_DATA = os.path.join(APP_ROOT, 'data')

def open_file(name):
    with open(os.path.join(APP_DATA, name)) as f:
        f.read()

def search_query(url):
    data = pull_profile(url)
    documents, dictionary, lsi, index = load_docs('linkedin',APP_DATA)
    logger.info(data)

    sims = query_docs(data, dictionary, lsi, index)

    #get 10 best matches
    idx = [sims[s][0] for s in range(0,10)]
    logger.info(idx)

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

    with open(os.path.join(APP_DATA, '%s-realidx.json' % name), 'r') as f:
        realidx = json.load(f)
    
    with open(os.path.join(APP_DATA, '%s-files.json' % name), 'r') as f:
        filelist = json.load(f)

    r = [filelist[realidx[i]] for i in indices]
    return r

def pull_linkedidx(indices):
    conn = db.connect('localhost', 'root', '1234', 'mydata')
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

