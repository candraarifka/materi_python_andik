## Modul & Package
#Modul adalah sebuah file yang berisikan sekumpulan kode fungsi dan global variabel yang disimpan dalam ekstensi .py.
#Sedangkan Package adalah sekumpulan modul yang memiliki constructur _init_ dalam satu folder.
# keduanya fungsinya sama yaitu menyisolasi baris code sesuai dengan kebutuhan.

##contoh
#struktur module dalam sebuah folder
#mygame/
#mygame/game.py
#mygame/draw.py

##penjelasan
#pada sebuah folder bernama mygame memiliki 2 file yaitu game.py dan draw.py. Kedua file tersebut bisa disebut dengan module
#baris code yang ada dalam file game.py, dapat dipanggil ke dalam file draw.py. Begitu pula sebaliknya

#struktur package dalam sebuah folder
#mygame/
#mygame/__init__.py
#mygame/game.py
#mygame/draw.py

#myplayer/
#myplayer/__init__.py
#myplayer/player.py

##penjelasan
# kita memiliki 2 buah folder yang didalamnya ada file python.
# keduanya sama-sama meliki file __init__.py, file tersebut berfungsi agar file dalam folder mygame bisa dipanggil oleh file dalam folder myplayer

##contoh pemanggilan
#module
#game.py

def get_level():
    print("level up 1 poin")

#draw.py
#import game
#game.get_level()

##penjelasan
#file draw.py memanggil function yang ada dalam module game.py, dengan cara import {"nama module"}, lalu panggil function dalam module tersebut tulis game.get_level()


##soal
#buatlah 2 module dalam satu folder beserta contoh pemanggilan modulenya
#buatlah 2 folder yang didalamnya file berisi function yang bisa saling memanggil
#(kata kunci=memanggil diurutkan dari nama_file-titik-nama_function)
