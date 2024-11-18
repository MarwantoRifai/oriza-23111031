import mysql.connector
from mysql.connector ImportError
try:
mydbs = mysql.connector.connect(
      host="127.0.3.1",
      user="root",
      password="",
      database = "dbsrita031"
)
mycursor = mydbs.cursor()
Entri_Data = """INSERT INTO Master VALUES ("A01","Notebook","Unit",5,7500000,"HP)"""
mycursor.execute(Entri_Data)
mydbs.commit()
print(mycursor.rowcount,  b  )