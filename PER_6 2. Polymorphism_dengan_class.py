# Polymorphism dengan class

class Kucing:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print("MEOW")

class Dog:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print("Guk....Guk")

kucing1 = Kucing("Tom", 3)
anjing1 = Dog("Spike",4)

for hewan in (kucing1,anjing1):
    hewan.bersuara()