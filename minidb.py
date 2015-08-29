import MySQLdb as mdb

def getInfo(index):
    db1 = mdb.connect(host="localhost",user="root", db="mydata")
    cur = db1.cursor()
    dict = {}
        cur.execute("SELECT Company,Title,Salary FROM Salaries WHERE Keywords=%s", (index))
        data = cur.fetchone()
    dict["Company"] = data[0]
    dict["Title"]=data[1]
    dict["Salary"] = data[2]
    return dict