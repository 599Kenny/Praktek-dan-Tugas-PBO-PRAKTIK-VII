# -*- coding: utf-8 -*-
"""PER 5. Program Hierarchical Inheritance Mahasiswa. 8

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qCEfbWnIx7YSmtOF7HtAnittDtST06Sk
"""

class Mahasiswa() :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim

class Siswa1(Mahasiswa) :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim
#5210411215      
    def detSiswa1(self) :
        print(self.nama, "Alamat : Wall Rose")

class Siswa2(Mahasiswa) :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim  
#5210411215
    def detSiswa2(self) :
        print(self.nama, "Jurusan : Informatika")

mahasiswa1 = Siswa1("Mikasa", 135105)
mahasiswa2 = Siswa2("Nezuko", 135117)

print(mahasiswa1.nim)   
mahasiswa1.detSiswa1()
print(mahasiswa2.nim)
mahasiswa2.detSiswa2()