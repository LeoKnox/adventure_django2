import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mysqladv"
)

mycursor = mydb.cursor()

sql = "UPDATE rooms SET width = 5"

mycursor.execute(sql)

sql = "UPDATE rooms SET length = 5"

mycursor.execute(sql)

mydb.commit()
#mycursor.execute("ALTER TABLE rooms ADD COLUMN width INT, ADD COLUMN length INT")

'''
sql = "INSERT INTO rooms (name, description) VALUES (%s, %s)"
val = ("Entry", "Entry way")

mycursor.execute(sql, val)

mydb.commit()
'''

#mycursor.execute("ALTER TABLE rooms ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#mycursor.execute("CREATE TABLE rooms (name VARCHAR(99), description VARCHAR(255))")