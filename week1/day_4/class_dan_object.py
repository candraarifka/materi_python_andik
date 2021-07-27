## Classes and Objects
# Class adalah sebuah teknik encapsulasi berbagai macam object. Object disini bisa berubah variable maupun function.
# Class berfungsi memudahkan pemanggilan object (variable atau function) secara berulang.
# referensi https://www.learnpython.org/en/Classes_and_Objects

## contoh
class MyClass:
    my_variable = "blah"

    def my_function(self):
        print("This is a message inside the class.")

#cara memanggil object (class variable dan class function) 
test = MyClass()

#memanggil class variable
print(test.my_variable)

#memanggil class function
test.my_function()

## penjelasan
# kita membuat sebuah class bernama MyClass yang didalamnya ada 2 buah object yaitu class variable & class function
# my_variable adalah class variable. my_function adalah class function

## soal
# buatlah sebuah class yang didalamnya ada class variable nama dan umur
# lalu buatlah class function untuk melakukan print seperti "nama saya {diisi nama} dan umur saya {diisi umur}"