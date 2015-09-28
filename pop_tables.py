import MySQLdb as db
import sys
import json

def populate_linkedin(joblist=None):
    conn = db.connect('localhost', 'root', '', 'glass')
    with conn:
        cur = conn.cursor()
        for j in joblist:
            cur.execute("INSERT INTO linkedin (company, title) VALUES (%s,%s)" %
                (j['company'], j['position']))
    con.close()

def populate_glassdoor(colist=None):
    conn = db.connect('localhost', 'root', '', 'glass')
    with conn:
        cur = conn.cursor()
        for c in colist:
            company = c.keys()[0]
            joblist = c[company]
            jobs = joblist.keys()
            for j in jobs:
                sals = joblist[j]
                if "Contractor" not in j and "Intern" not in j:
                    try:
                        cur.execute('INSERT INTO glassdoor (company,title,count,max_sal,min_sal,mean_sal) VALUES (\"%s\",\"%s\",%d,%d,%d,%d)' %
                            (company, j.replace("/", "-"), to_int(sals["count"]),
                                to_int(sals["max"]),
                                to_int(sals["min"]),
                                to_int(sals["mean"]) ))
                    except:
                        print "(%s,%s,%d,%d,%d,%d)" % (company, j.replace("/", "-"), sals["count"],
                                to_int(sals["max"]),
                                to_int(sals["min"]),
                                to_int(sals["mean"]))
                    #return
    conn.close()

def to_int(sal):
    if isinstance( sal, ( int, long ) ):
        return sal
    s = sal.encode('ascii','ignore')
    try:
        return int(filter(str.isdigit, s))
    except:
        print s
        return 0

# run it
json_file='clean_glassdoor.json'
json_data=open(json_file)
data = json.load(json_data)
json_data.close()
populate_glassdoor(data)
