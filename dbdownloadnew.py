import os
import crypt
import MySQLdb
def db():
	try:
	   ip=raw_input("Enter the Storage IP ::: ")
	   s=raw_input("Enter the server name ::: ")
	   db=raw_input("Enter the db name ::: ")
	   dt=raw_input("Enter the date ::: ")
	   mth=raw_input("Enter the month ::: ")
	   yr=raw_input("Enter the year ::: ")
	   password="Cy!@Hih4cobaQofu"
	   os.system("sshpass -p "+password+" scp root@"+ip+":/home/backup/array1/backup/"+s+"/db/"+db+"/"+dt+mth+".sql.gz /home/manish/Desktop/")
   	   conn=MySQLdb.connect(user='root', passwd='123', host='192.168.9.99')
	   cursor = conn.cursor()
	   sql = 'CREATE DATABASE IF NOT EXISTS mydata'
	   cursor.execute(sql)
	   conn1=MySQLdb.connect(user='root', passwd='123', db='mydata', host='192.168.9.99')
	   cursor = conn1.cursor()
	   os.system("gunzip /home/manish/Desktop/"+dt+mth+".sql.gz")
	   os.chdir("/home/manish/Desktop/")
	   os.system("mysql -w -f mydata -h 192.168.9.99 -uroot -p123 --verbose < "+dt+mth+".sql")
	except IOError:
           print ("I/O Error")
db()
