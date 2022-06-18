#Setahu saya list itu adalah sebuah variabel yang bisa menampung berbagai macam tipe data 
#Sedangkan Linked list adaalh banyaknya variabel yang dihibungkan jadi seperti rantai  

class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None
    
    #Method ini digunakan untuk mengecek apakah ada element atau node dalam linked  
    def traverse_list(self):
        #Jika self.star_node adalah kosong maka linked list tidak memiliki element 
        if self.start_node is None:
            print("List has no element")
            return
        #Dan jika tidak kosong maka akan masuk di else dan akan diproses
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.ref

    #Method ini berfungsi untuk memasukan nilai atau node diawal linked list 
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node
    
    #Method ini berfungsi untuk memasukkan nilai atau node diakhir linked list 
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n= n.ref
        n.ref = new_node;
    
    def get_tail(self):
        n = self.start_node
        while n.ref is not None:
            n = n.ref
            self.tail = n
        return self.tail

                            ### SOAL TUGAS Linked List ###
# 1. Buatlah method untuk mencari banyaknya anggota sebuah linked list
    def BanyakAnggota(self):
        if self.start_node is None:
            print("list has not element")
            return

        n = self.start_node
        Banyak = 0
        while n is not None:
            Banyak += 1
            n = n.ref
        return Banyak

# 2. Buatlah method untuk menghitung jumlah (sum) semua bilangan di sebuah linked list
    def Jumlah(self):
        if self.start_node is None:
            return

        Jumlah = 0
        n = self.start_node
        while n is not None:
            Jumlah += n.item
            n = n.ref
        return Jumlah 

# 3. Buatlah method untuk menyambung dua buah linked list menjadi sebuah linked list. 
#    Pengguna bisa menetukan susunannya apakah linkedlist1linkedlist2 atau linkedlist2linkedlist1
    def Sambung(self, linked_list2, x = 1):
        if x == 1:
            self.get_tail()
            self.tail.ref = linked_list2.start_node
        
        elif x == 2:
            linked_list2.get_tail()
            linked_list2.tail.ref = self.start_node
            self.start_node = linked_list2.start_node

# 4. Buatlah method untuk menambahkan data ke linkedlist sedemikian hingga data 
#    yang ada di linkedlist dalam kondisi terurut
    def Mengurutkan(self):
        end = None
        while self.start_node.ref != end:
            y = self.start_node
            while y.ref != end:
                ref = y.ref
                if y.item > ref.item:
                    y.item, ref.item = ref.item, y.item
                y = y.ref
            end = y

# 5. Buatlah method untuk membalik arah semua pointer di linkedlist
    def Membalik(self) :
        end_z = None
        z = self.start_node
        x = None
        while z:
            ref = z.ref
            z.ref = x
            x = z
            z = ref
            self.start_node = x


print("Node Linked List 1: ")
Data = LinkedList()
Data.insert_at_start(12)
Data.insert_at_start(2)
Data.insert_at_start(6)
Data.insert_at_start(10)
Data.insert_at_start(30)
Data.insert_at_start(1)

Data.traverse_list()
print("\n")

print("Node Linked List 2: ")
Data2 = LinkedList()
Data2.insert_at_start(55)
Data2.insert_at_start(23)
Data2.insert_at_start(9)
Data2.insert_at_start(76)
Data2.insert_at_start(38)
Data2.insert_at_start(90)

Data2.traverse_list()

print("===============================")
print("Banyak anggota Linked List:", Data.BanyakAnggota())

print("Jumlah semua anggota yang ada di Linked List:", Data.Jumlah())

print("Penyambungan Linked List 1 dan Linked List 2 :")
Data.Sambung(Data2)
Data.traverse_list()

print("Mengurutkan anggota yang ada di linked list 1:")
print("Sebelum diurutkan: ")
Data.traverse_list()
print("Sesudah diurutkan: ")
Data.Mengurutkan()
Data.traverse_list()

print("Mengurutkan anggota yang ada di linked list 2:")
print("Sebelum diurutkan: ")
Data2.traverse_list()
print("Sesudah diurutkan: ")
Data2.Mengurutkan()
Data2.traverse_list()

print("Membalikkan arah semua pointer di linked list:")
print("Sebelum membalikkan arah: ")
Data.traverse_list()
Data.Membalik()
print("Sesudah membalikkan arah: ")
Data.traverse_list()

print("\n")
