# memanggil fungsi pada Koneksi.py
import mysql.connector
import pymysql
import serial
import koneksi
konek = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="arduino_python"
)

cursor = koneksi.konek.cursor()
sql = "SELECT * FROM arduino_python.lcd_arduino"

cursor.execute(sql)

results = cursor.fetchall()

for data in results :
   print(data)


