# memanggil fungsi pada Koneksi.py
import koneksi
from koneksi import cursor

qry = cursor.execute("""CREATE TABLE arduino_python.lcd_arduino  ( ISI VARCHAR(50) )""")

if qry:
    print("table berhasil dibuat")
#informasi yang ditampilkan ketika perintah gagal
else:
    print("table gagal dibuat")


