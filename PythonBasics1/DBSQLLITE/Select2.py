from conn import getConn

con =getConn()
cursor = con.cursor()

#fetch only id,name from all persons
print("conn success")
sql1 = "SELECT ID,NAME  FROM person  "
cursor.execute(sql1)
myresult = cursor.fetchall()

for row in myresult:
   print(row)

if cursor:
  cursor.close()
if con:
  con.close()