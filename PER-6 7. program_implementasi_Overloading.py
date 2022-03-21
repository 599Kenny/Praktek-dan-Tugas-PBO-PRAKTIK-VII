class Mahasiswa:
    def __init__(self,nama,nim,prodi,thn_masuk,semester):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk
        self.semester = semester

    def tampilMhs(self):
        print(f"Nama\t\t: {self.nama} \nNim\t\t: {self.nim}  \nprodi\t\t: {self.prodi} \nthn_masuk\t: {self.thn_masuk} \nsemester\t: {self.semester}\n")

    #Overloading
    def hitungSKS(self,jmlsks=None, sks=None):
        if jmlsks !=None and sks!=None:
            totalsks = jmlsks + sks
            print("Total sks = ",totalsks)
        else:
            totalsks = jmlsks
            print("Total SKS =", totalsks)

#Memanggil
mhs1 = Mahasiswa("Eren", 240, "Teknik Sipil", 20220, 4)
mhs2 = Mahasiswa("Luffy", 229, "INFORMATIKA", 2021, 2)
mhs1.tampilMhs()
mhs2.tampilMhs()
mhs1.hitungSKS(80,34)
mhs2.hitungSKS(89)
    
