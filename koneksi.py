import mysql.connector
mydbs=mysql.connector.connect(
    host= "127.0.3.1",
    user= "root",
    database=""
)
xcursor=mydbs.cursor()
xcursor.execute("CREATE DATABASE dbskita031")
print("database berhasil")