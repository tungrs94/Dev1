import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="TUNG",
    password="",
    db='mydatabase'
)
cursor = mydb.cursor()
cursor.execute("DROP TABLE IF EXISTS customer")
create_table = '''CREATE TABLE customer(
                customerid VARCHAR(255),
                firstname VARCHAR(255),
                lastname VARCHAR(255),
                companyname VARCHAR(255),
                billingaddress1 VARCHAR(255),
                billingaddress2 VARCHAR(255),
                city VARCHAR(255),
                state VARCHAR(255),
                postalcode VARCHAR(255),
                country VARCHAR(255),
                phonenumber VARCHAR(255),
                emailaddress VARCHAR(255),
                createddate VARCHAR(255)
                )'''

cursor.execute(create_table)

with open('customer.csv') as f:
    data = csv.reader(f)
    for row in data:
        cursor.execute('INSERT INTO customer(customerid, firstname, lastname, companyname, billingaddress1, billingaddress2, city, state, postalcode, country, phonenumber, emailaddress, createddate) VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")', row)

mydb.commit()
cursor.close()
print('Done')