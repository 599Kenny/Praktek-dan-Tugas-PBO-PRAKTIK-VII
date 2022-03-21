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
        print("\nTampil dari sub class Processor")
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Harga\t\t: {self.harga}")

class RandomAccessMemory(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas) :
        super().__init__(pabrikan, nama, harga)
        self.kapasitas = kapasitas

    # Metode OverRidding
    def Tampil(self) :
        print("Tampil dari sub class RandomAccessMemory")
        print(f"{self.nama} produk dari {self.pabrikan}\nKapasitas\t: {self.kapasitas}")
        print(f"Harga\t\t: {self.harga}")

class HardDiskSATA(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm) :
        super().__init__(pabrikan, nama, harga)
        self.kapasitas = kapasitas
        self.rpm = rpm 

    #Metode OverOverring
    def Tampil(self) :
        print("Tampil dari sub class HardDiskSATA")
        print(f"{self.nama} produk dari {self.pabrikan}\nKapasitas\t: {self.kapasitas}")
        print(f"RPM\t\t: {self.rpm}\nHarga\t\t: {self.harga}")

p = Processor('Intel', 'Core i7 7740X', 4350000)
ram = RandomAccessMemory('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, "4GB")
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)

parts = [p, ram, hdd]  
print("\n\t\t\tOVERRIDING COMPUTER PART")
print("=================================================================================")
for part in parts :
    part.Tampil()
    print("")
print("=================================================================================\n")