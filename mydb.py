import mysql.connector

db = mysql.connector.connect(
    
    host= 'localhost',
    user = 'root',
    passwd = 'password123',
    database = 'ethio_therapy_db',
    
)

cursor = db.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS dcrm')

print('Created database')