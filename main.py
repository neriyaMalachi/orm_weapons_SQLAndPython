import mysql.connector

cnx = mysql.connector.connect(
    user="root",
    password="",
    host="127.0.0.1",
    database="classicmodels"
)

print("Connected! Server version:", cnx.get_server_info())

cursor = cnx.cursor()

cursor.execute("SELECT * FROM customers")

data=  cursor.fetchall()


cursor.close()
cnx.close()
