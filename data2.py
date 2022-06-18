#SOAL NOMER 3
class AntrianBank: 
    def __init__(self, panggil, antrian):
        self.panggil = panggil
        self.antrian = antrian

    def UpPanggil(self):
        if self.panggil == self.antrian:
            pass 
        else: 
            self.panggil += 1

    def UpAntrian(self):
        self.antrian += 1

    def Reset(self):
        self.panggil = 0
        self.antrian = 0

    def GetPanggil(self):
        return self.panggil

    def GetAntrian(self):
        return self.antrian

Bank = AntrianBank(0, 0)

Bank.UpAntrian()
Bank.UpAntrian()
Bank.UpAntrian()

Bank.UpPanggil()
Bank.UpPanggil()
Bank.UpPanggil()
Bank.UpPanggil()

Bank.UpAntrian()
Bank.UpPanggil()

print("Total antrian:", Bank.GetAntrian())
print("Total panggil:", Bank.GetPanggil())