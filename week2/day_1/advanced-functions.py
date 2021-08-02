## args, kwargs, return & lambda pada function
#Fungsi di python adalah block code yang bisa menggunakan nol atau lebih argumen/parameter dan mengembalikan nilai.
#Python cukup fleksibel dalam hal bagaimana argumen diteruskan/masukkan ke suatu fungsi.
#*args dan **kwargs membuatnya lebih mudah dan clean untuk menggunakan argumen.

## contoh args
def addition(*args):
   result = 0
   for i in args:
      result += i
   print(result)

addition()
addition(1,4)

## pembahasan
# args bisa digunakan untuk mengisi argumen di sebuah fungsi
# terkadang kita membutuhkan argumen yang banyak disebuah fungsi, contoh test(1,2,3,4,5,6), tapi kita bisa hanya menuliskan test(args)

## soal
# buatlah contoh penggunaan args pada sebuah function

## contoh kwargs
def arg_printer(**kwargs):
    print(kwargs.get("param1"))
    print(kwargs.get("param2"))
    
arg_printer(param1=5, param2=6)

## pembahasan
# kwargs juga bisa disebut keyword argumen
# bedanya dengan args, kwargs menggunakan format key & value

## soal
# buatlah contoh penggunaan kwargs pada sebuah function

## contoh return
def hitung_luas_segitiga(alas, tinggi):
  luas = (alas * tinggi) / 2
  return luas
    
var1 = hitung_luas_segitiga(5, 7)
print("Luas segitiga adalah:",var1)
print("Luas segitiga kali 2", var1*2)

## pembahasan
#Kenapa return?
#Karena kita tidak selamanya ingin menampilkan text di cmd. Karena fungsi print hanya melakukan menampilkan text.
#Dalam banyak situasi, hasil sebuah function perlu disimpan ke dalam variabel terlebih dahulu, untuk kemudian di proses lebih lanjut.
#Untuk keperluan inilah perlu menambah perintah return ke dalam function. Tujuannya, agar sebuah function bisa mengembalikan nilai.

## soal
# buatlah contoh penggunaan return pada sebuah function


## contoh lambda function
x = lambda a, b : a * b
print(x(5, 6))

n = x(2,3)
print(n)
## pembahasan
# lambda function juga sering disebut fungsi tanpa nama.
# biasanya digunakan pada fucntion2 sederhana
# menggunakan syntax lambda, lalu diikuti argumen dan operator untuk dijadikan output

## soal 
# buatlah contoh penggunaan lambda pada sebuah function
