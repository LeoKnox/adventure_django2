import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="passroot",
    database="mydatabase"  # if database doesn't exist an error will occur
)

mycursor = mydb.coursor()

sql = "SELECT \
    characters.name AS character \
    weapon.name AS weapon \
    FROM characters \
    RIGHT JOIN weapon ON characters.weap = weapon.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

'''
mycursor.execute("SELECT * FROM characters LIMIT OFFSET 2")

#mycursor.execute("SELECT * FROM characters LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
'''
'''
sql = "UPDATE characters SET  char_class=%s WHERE name=%s"
val = ("Warrior", "Elric")

mycursor.execute(sql, val)

mydb.commit()

mycursor.execute(sql)

mydb.commit()
'''

'''
sql = "DELETE FROM characters WHERE name = %s"  # without WHERE all characters deleted
char_name = ("Frogman")     # use with %s to prvent sql injection

mycursor.execute(sql, char_name)

mydb.commit()       # no commit no delete

print(mucursor.rowcount, "record deleted")
'''

'''
mycursor.execute("SELECT * FROM characters ORDER BY char_class DESC")

myresult = mycursor.fetchall()

sql = "SELECT name, char_class FROM characters WHERE name = %s"
char_class = ("Elric")

mycursor.execute(sql, char_class)

mysingle = mycursor.fetchone()

print(mysingle)

for x in myresult:
    print(x)
'''

'''
sql = "INSERT INTO characters (name, char_class, lvl) VALUES (%s, %s, %s)"
val = ("Elric", "Albino", 8)
mycursor.execute(sql, val)

mydb.commit()
'''
#print("1 character inserted, Char ID: ", mycursor.lastrowid)

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