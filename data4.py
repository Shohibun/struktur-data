#SOAL NOMER 1
def Segitiga():
    Sisi_A = float(input("Masukkan besar sisi A: "))
    Sisi_B = float(input("Masukkan besar sisi B: "))
    Sisi_C = float(input("Masukkan besar sisi C: "))

    print("---------------------Segitiga Siku-Siku------------------------")
    #Disini saya menggunakan rumus phytagoras
    #Disini rumus yang saya gunakan disetiap sisi sama karena inputan dari user tidak selalu sisi C yang paling besar
    #Disini saya menggunakan float kaerna takutnya user menginputkan bilangan decimal  
    if Sisi_C**2 == Sisi_A**2 + Sisi_B**2:
        print("Benar") 
    elif Sisi_A**2 == Sisi_B**2 + Sisi_C**2:
        print("Benar")
    elif Sisi_B**2 == Sisi_A**2 + Sisi_C**2:
        print("Benar")
    else: 
        print("Salah")

Segitiga()

print("--------------------------------------------------------------------------------------------------------")

#SOAL NOMER 2
def Urutan():
    print("Inputan isi List:")
    Data = input()
    DataFix = [float(i) for i in Data.split()]
    Max = len(DataFix)

    #Disini kita harus mengurutkan terlebih dahulu pakek Buble Sort 
    #Setelah itu kita bisa mencari selisih bilangan terbesar dengan terkecil
    for x in range(Max-1, 0,-1):
        for y in range(x):
            if DataFix[y] > DataFix[y+1]:
                DataFix[y], DataFix[y+1] = DataFix[y+1], DataFix[y]
    Hasil = DataFix[Max-1] - DataFix[0]
    print("------------------------Selisih Bilangan Terbesar dengan Tekecil--------------------------")
    print("Hasil:", Hasil)

Urutan()