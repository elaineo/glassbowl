# import MySQLdb as db
from query_tools import *
import requests

def search_query(url):
    data = pull_profile(url)
    documents, dictionary, lsi, index = load_docs('linkedin')

    sims = query_docs(data, dictionary, lsi, index)

    #get 10 best matches
    idx = [sims[s][0] for s in range[0:10]]

    results = pull_linkedidx(idx)


def pull_linkedidx(indices):
    conn = db.connect('localhost', 'root', '', 'mydata')
    with conn:
        cur = conn.cursor()
        results = []
        for idx in indices:
            query = "select company, title from linkedin where id = %s" % idx
            cur.execute(query)
            res = cur.fetchone()
            results.append(res.fetchone())
    conn.close()
    return results
