#OverRidding ComputerParts
class ComputerPart:
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga

class Processor(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga
            
    def Tampil(self) :
        print("\nProcessor")
        print(f"Nama Barang  : {self.nama}")
        print(f"produk dari  :  {self.pabrikan}")
        print(f"Harga        : {self.harga}")

class RandomAccessMemory(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama  
        self.harga = harga

    #Overload Method
    def Tampil(self, kapasitas) :  
        print("\nRandomAccessMemory")
        print(f"Nama Barang  : {self.nama}")
        print(f"produk dari  :{self.pabrikan}")
        print(f"Kapasitas\   : {kapasitas}")
        print(f"Harga        : {self.harga}")

class HardDiskSATA(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama  
        self.harga = harga

    #Overload Method
    def Tampil(self, kapasitas, rpm) : 
        print("\nHardDiskSATA")
        print(f"Nama Barang : {self.nama}")
        print(f"produk dari : {self.pabrikan}")
        print(f"Kapasitas   : {kapasitas}")
        print(f"RPM         : {rpm}")
        print(f"Harga       : {self.harga}")


p = Processor('Intel', 'Core i7 7740X', 4350000)
ram = RandomAccessMemory('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000)
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000)

print("----------------------------------------------------------------------------------")
print("------------------------OVERLOADING COMPUTER PART---------------------------------")
print("__________________________________________________________________________________")
p.Tampil()
ram.Tampil("4GB")
hdd.Tampil("500GB", 7200)
print("__________________________________________________________________________________")