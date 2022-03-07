# -*- coding: utf-8 -*-
"""PER_4_Latihan_8_sampai_10_5210411240_RIVALDI_KENNY_N_PBO_7

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OAKAKxnEKZr-RfKwkBcy2EdNouxOgX5o

Nama : Rivaldi Kenny N

NIM : 5210411240

Kelas : PBO Praktik

TUGAS PBO PRAKTIK VII

Class Menu
"""

class Menu:
  def __init__(self,nama,deskripsi,harga,Rank,Alamat):
    self.nama = nama
    self.deskripsi = deskripsi
    self.__harga = harga
    self.__Rank = Rank
    self.Alamat = Alamat

mm1 = Menu('jus jambu','jus jambu merah tanpa gula',8500,6,'Jl.Asam Urat')
mm2 = Menu('jus alpukat ori','jus alpukat dengan tambahan air gula merah',15000,5,'Jl Pelita')
mm3 = Menu('jus alpukat extra susu','jus alpukat dengan campuran susu coklat dan taburan kepingan choco',15000,4,'Jl. Aqua')
mm4 = Menu('red & smooth','smoothie pisang susu dengan strawberry',175000,3,'Jl. Kaliurang')
mm5 = Menu('Bakso','Bakso bukan sembarang bakso dibuat dengan DAGING SAPI DAN DAGING TITAN COLOSAL',45000,2,'Jl. Gung')
mm6 = Menu('Ceker Setan Dan Seblak Kunti','Bahannya diambil Langsung dari dunia lain',100000,1,'Jl. Berkah')

Pilihan_minuman = [mm1,mm2,mm3,mm4,mm5,mm6]
print('Daftar_menu Makanan TER')
for mn in Pilihan_minuman:
  t = '{}.{} harga Rp {}, {}.{}' .format(mn._Menu__Rank,mn.nama,mn._Menu__harga,mn.deskripsi,mn.Alamat)
  print()
  print(t)

"""Class Mahasiswa"""

class Mahasiswa:
  def __init__(self,nama,nim,prodi,thn_masuk,umur,asal):
    self.nama = nama
    self.nim = nim
    self.prodi = prodi
    self.__thn_masuk = thn_masuk
    self.__umur = umur
    self.__asal = asal

m1 = Mahasiswa('Udin','10120371','sistem Informasi',2020,23,'Surabaya')
m2 = Mahasiswa('Rivaldi',5210411,'Teknik Informatika',2021,19,'Sampit')
m3 = Mahasiswa('Kenny',240,'Informatika',2022,19,'Kotawaringin Timur')

list_mahasiswa = [m1,m2,m3]
print(' DAFTAR MAHASISWA ')
for m in list_mahasiswa:
  teks = '{} dengan umur {} adalah mahasiswa {} angkatan {} berasal dari {} dengan nim {}'.format(m.nama,m._Mahasiswa__umur,m.prodi,m._Mahasiswa__thn_masuk,m._Mahasiswa__asal,m.nim)
  print()
  print(teks)

"""Class Buku"""

class Buku: 
  def __init__(self,judul,pengarang,tahun_terbit,penerbit,harga):
    self.judul = judul 
    self.pengarang = pengarang
    self.tahun_terbit = tahun_terbit
    self.penerbit = penerbit
    self.__harga = harga

buku1 = Buku('Tenggelamnya Kapal Van Wijck','HAMKA',1938,'Nusantara',150000)
buku2 = Buku('Majalah Bobo','Tim Gramedia',1973,'GRAMEDIA',30000)
buku3 = Buku('Harry Potter','J.K. Rowling',1997-2007,'	Bloomsbury Publishing dan Scholastic Press',199000)

daftar_buku = [buku1,buku2,buku3]
print('List BUKU')
for buku in daftar_buku:
  t = '- buku {} karangan {} dan penerbit {} pertman kali diterbitkan tahun {} dibandrol dengan harga {}' .format(buku.judul,buku.pengarang,buku.penerbit,buku.tahun_terbit,buku._Buku__harga)
  print()
  print(t)