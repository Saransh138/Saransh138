import pymysql

#connection object
mydb = pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="health_insurance")

#cursor object
mycursor = mydb.cursor()
