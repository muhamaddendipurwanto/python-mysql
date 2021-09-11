# mengimport serial library
import serial

# memanggil fungsi pada Koneksi.py
import mysql.connector
import pymysql
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
# membuat serial port object bernama ambilDataAngka
# samakan port dan baut rate seperti di arduino
ambilDataAngka = serial.Serial('com10',9600)
 
# loop terus menerus
while (1==1):
 
# apakah ada data yang dikirimkan ? jika ya baca data
    if (ambilDataAngka.in_waiting>0):
 
# baca data
        dataHasil = ambilDataAngka.readline()
 
# print hasil baca data
        print (dataHasil)
