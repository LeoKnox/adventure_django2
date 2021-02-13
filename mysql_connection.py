import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="passroot",
    database="mydatabase"  # if database doesn't exist an error will occur
)

mycursor = mydb.coursor()

sql = "INSERT INTO characters (name, char_class, lvl) VALUES (%s, %s, %s)"
val = ("Elric", "Albino", 8)
mycursor.execute(sql, val)

mydb.commit()

#mycursor.execute("ALTER TABLE characters ADD COLUMN lvl INT")

#mycursor.execute("CREATE TABLE characters (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), char_class VARCHAR(255))")

'''
mycursor.Execute("SHOW TABLES")

for y in mycursor:
    print(y)
'''

#mycursor.execute("CREATE TABLE customer (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("CREATE DATA mydatabase")

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
#    print(x)