import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="passroot"
)

mycursor = mydb.coursor()

mycursor.execute("CREATE DATA mydatabase")