import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'

)

#prepare cursor object
cursorObject = dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE MagnaCo")

print('All Done!')