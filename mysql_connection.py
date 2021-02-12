import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="passroot",
    database="mydatabase"  # if database doesn't exist an error will occur
)

mycursor = mydb.coursor()

mycursor.Execute("SHOW TABLES")

for y in mycursor:
    print(y)
    
#mycursor.execute("CREATE TABLE customer (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("CREATE DATA mydatabase")

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
#    print(x)