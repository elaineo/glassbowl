# -- coding: utf-8 --

import json
from pprint import pprint
import MySQLdb as mdb


json_file='clean_glassdoor.json'

json_data=open(json_file)
data = json.load(json_data)
json_data.close()
#pprint(data)

def getInfo(index):
	dict = {}
        cur.execute("SELECT Company,Title,Salary FROM Salaries WHERE Keywords=%s", (index))
        data = cur.fetchone()
	dict["Company"] = data[0]
	dict["Title"]=data[1]
	dict["Salary"] = data[2]
    return dict


db1 = mdb.connect(host="localhost",user="root", db="mydata")
cur = db1.cursor()

#create table
with db1:
    
    cur.execute("DROP TABLE IF EXISTS Salaries")
    cur.execute("CREATE TABLE Salaries(Company VARCHAR(255), Title VARCHAR(255), Salary VARCHAR(255), Keywords INTEGER(255) AUTO_INCREMENT, PRIMARY KEY (Keywords))")

    for i in range(len(data)):
    	company = data[i]
	company_name = company.keys()[0]
	print company_name
	titles = company[company_name]
	all_titles = titles.keys()
	for title in all_titles:
	    	print title
	    	record = titles[title]
		title = title.encode('latin-1', errors='replace')
		cur.execute("INSERT INTO Salaries(Company, Title, Salary) VALUES(%s, %s, %s)", (company_name, title.replace("/", "-"), record["max"]))

#dict = getInfo("1")
#print dict["Company"]
#print dict["Title"]
