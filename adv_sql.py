import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mysqladv"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE characters (name VARCHAR(99), description VARCHAR(255))")