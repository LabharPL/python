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


mycursor = mydb.cursor()

# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   INNER JOIN products ON users.fav = products.id"

sql = "SELECT   users.name AS user,   products.name AS favorite   FROM users  JOIN products ON users.fav = products.id"






mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)