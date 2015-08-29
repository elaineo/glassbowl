import json
from pprint import pprint
import MySQLdb as mdb

json_file='glassdoor_list.json'

#json_file='test.json'
json_data=open(json_file)
data = json.load(json_data)
json_data.close()
#pprint(data)

#for company in data
  #place in DB

db1 = mdb.connect(host="localhost",user="root", db="mydata")

#cursor= db1.cursor()
#sql = 'CREATE DATABASE mydata'
#cursor.execute(sql)

#create table
with db1:
    
    cur = db1.cursor()
    cur.execute("DROP TABLE IF EXISTS Salaries")
    cur.execute("CREATE TABLE Salaries(Company VARCHAR(255), Title VARCHAR(255), Salary VARCHAR(255), Keywords INTEGER(255) AUTO_INCREMENT, PRIMARY KEY (Keywords))")

    for i in range(len(data)):
    	company = data[i]
	company_name = company.keys()[0]
	print company_name
	titles = company[company_name]
	all_titles = titles.keys()
	for title in all_titles:
	    	#print title
	    	record = titles[title]
	    	#print record
	    	#print("INSERT INTO Salaries(Company) VALUES(\"" + company + "\")")
	    	cur.execute("INSERT INTO Salaries(Company, Title, Salary) VALUES(\"" + company_name + "\", \""+ title.replace("-", "/") + "\", \"" + record["max"]+ "\")")
