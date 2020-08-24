import mysql.connector
import csv
with open('customer.csv') as f:
    data = csv.DictReader(f)

mydb = mysql.connector.connect(host="localhost", user='TUNG',
                               passwd='')

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")