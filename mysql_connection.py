import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="passroot",
    database="mydatabase"  # if database doesn't exist an error will occur
)

mycursor = mydb.coursor()

# mycursor.execute("CREATE DATA mydatabase")

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
#    print(x)