def Palindrom(MyList):
    #Rumus awal dari Palindrom
    if len(MyList) == 0 or len(MyList) == 1:
        print("True")
    #Palindrom adalah suatu bilangan jika indeks depan dan belakang nilainya sama
    elif MyList[0] == MyList[-1]:
        ListBaru = MyList[1:-1]
        print(ListBaru)
        return Palindrom(ListBaru)
    else:
        print("False")
MyList1 = [1, 2, 3, 4, 4, 3, 2, 1]

Palindrom(MyList1)
