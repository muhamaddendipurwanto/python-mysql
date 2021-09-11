# memanggil fungsi pada Koneksi.py
import koneksi
from koneksi import cursor


txt_lcd = input("ISI: ")
val = (txt_lcd)

cursor = koneksi.konek.cursor()
sql = "INSERT INTO arduino_python.lcd_arduino (ISI) VALUES (%s)"

cursor.execute(sql, val)
koneksi.konek.commit()
print("{} data berhasil disimpan".format(cursor.rowcount))