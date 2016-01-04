import MySQLdb as mdb

def getInfo(index):
    db1 = mdb.connect(host="localhost",user="root",passwd="1234", db="mydata")
    cur = db1.cursor()
    dict = {}
    cur.execute("SELECT Company,Title,Salary FROM Salaries WHERE Keywords=%s", (index))
    data = cur.fetchone()
    dict["Company"] = data[0]
    dict["Title"]=data[1]
    dict["Salary"] = data[2]
    return dict

def getSalary(dict_list):
    db1 = mdb.connect(host="localhost",user="root",passwd="1234", db="mydata")
    cur = db1.cursor()
    dict_out_list = []
    for dict in dict_list:
    	dict_out ={}
        company = dict["Company"]
        title = dict["Title"]
        cur.execute("SELECT Company,Title,Salary FROM Salaries WHERE Company=%s AND Title=%s", (company, title))
        data = cur.fetchone()
        if data:
            dict_out["Company"] = data[0]
            dict_out["Title"]=data[1]
            dict_out["Salary"]=data[2]
            dict_out_list.append(dict_out)
    return dict_out_list
