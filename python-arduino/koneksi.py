#import / tambahkan library pymysql.cursor
import pymysql.cursors
# Koneksi ke database
konek = pymysql.connect(host='localhost',
                 user='root',
                 password='',
                 cursorclass=pymysql.cursors.DictCursor)
# siapkan objek kursor menggunakan metode cursor()
cursor = konek.cursor()

if cursor:
    print("Berhasil koneksi ke database")