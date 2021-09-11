# memanggil fungsi pada Koneksi.py
import koneksi
from koneksi import cursor
# Perintah membuat database
buat_db = cursor.execute("CREATE DATABASE arduino_python")
# Informasi yang ditampilkan ketika perintah berhasil
if buat_db:
    print("Database berhasil dibuat!")
# Informasi yang ditampilkan ketika perintah gagal
else:
    print("Database gagal dibuat")