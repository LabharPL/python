#  <?php
# $servername = "s34.linuxpl.com";
# $username = "arekh_mqtt";
# $password = "Lublewo@12";
# $dbname = "arekh_mqtt";
#
# // Create connection
# $conn = new mysqli($servername, $username, $password, $dbname);
# // Check connection
# if ($conn->connect_error) {
#     die("Connection failed: " . $conn->connect_error);
# }
#
# $sql = "INSERT INTO test (Field, timnestamp)
# VALUES ('2', '12'')";
#
# if ($conn->query($sql) === TRUE) {
#     echo "New record created successfully";
# } else {
#     echo "Error: " . $sql . "<br>" . $conn->error;
# }
#
# $conn->close();
# ?>


import mysql.connector

mydb = mysql.connector.connect(
  host="s34.linuxpl.com",
  user="arekh_mqtt",
  passwd="Lublewo@12",
  database="arekh_mqtt"
)

serv = mysql.connector.connect(
  host="s34.linuxpl.com",
  user="arekh_mqtt",
  passwd="Lublewo@12",
  # database="arekh_mqtt"
)



import config

mycursor = mydb.cursor()

sql = "INSERT INTO test (Field, timestamp) VALUES (%s, %s)"
val = ("2", "21")
# mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


# nowe


# mycursor = mydb.cursor()
#
# sql = "DELETE FROM test WHERE Field = '2'"
#
# mycursor.execute(sql)
#
# mydb.commit()

#print(mycursor.rowcount, "record(s) deleted")

mycursorread = mydb.cursor()

mycursorread.execute("SELECT * FROM test")

myresult = mycursorread.fetchall()

# for x in myresult:
#   print (x)


print(mycursorread.rowcount, "record read.")

print(mydb)

c = serv.cursor()

print('a teraz show')

print (c)
print c.execute("SHOW DATABASES")

# print (c)

print('database done')

l = c.fetchall()
print l
l = [ i[0] for i in l ]
print l

# c.execute("select database();")


db = lambda(db): mysql.connector.connect(host="s34.linuxpl.com",user="arekh_mqtt",passwd="Lublewo@12",db=db)

print(mydb)

mydb = db("arekh_Node-RED-test")

print(mydb)

cursor = mydb.cursor()


sqlstring = 'SHOW TABLES;'
# cursor.execute('USE CustDB')
x = cursor.execute(sqlstring)
print('tu sywnik show tables')
print(x)


# raw_input("Press Enter to continue...")



tables = cursor.fetchall()
print(tables)

cursor.execute("SELECT * FROM test ORDER BY Field DESC LIMIT 15 OFFSET 123456")


myresult = cursor.fetchall()

for x in myresult:
  print (x)

print(cursor.rowcount, "record read.")

