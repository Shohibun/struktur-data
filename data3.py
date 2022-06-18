#SOAL NOMER 4
class TitikDuaD:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def geserHorizontal(self, dx):
        self.x += dx

    def geserVertikal(self, dy):
        self.y += dy
    
    def hitungJarak(self, titikLain):
        Jarak = ((titikLain.x - self.x)**2 + (titikLain.y - self.y)**2)**0.5
        return Jarak

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

titik1 = TitikDuaD(2, 3)
titik2 = TitikDuaD(4, 5)
titik1.geserHorizontal(-3)
titik1.geserVertikal(-7)
print(f"Koordinat t1: {titik1.getX()}, {titik1.getY()}")
titik2.geserHorizontal(15)
titik2.geserVertikal(9)
print(f"Koordinat t2: {titik2.getX()}, {titik2.getY()}")
print(f"Hasil jarak t1 dengan t2: {titik1.hitungJarak(titik2)}")
