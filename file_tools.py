from os import listdir
from os.path import isfile, join, isdir
import MySQLdb as db

dirs = [ './data/'+f for f in listdir('./data/') if isdir(join('./data/',f)) ]
filelist = []
for d in dirs:
    files = [ d+'/'+f for f in listdir(d) if isfile(join(d+'/',f)) ]
    filelist += files

populate_linkedin(filelist)

def populate_linkedin(joblist=None):
    conn = db.connect('localhost', 'root', '', 'mydata')
    with conn:
        cur = conn.cursor()
        for f in filelist:
            j = f.split('/')
            query = "INSERT INTO linkedin (company, title) VALUES (\"%s\",\"%s\")" % (j[2], j[3])
            cur.execute(query)
    conn.close()