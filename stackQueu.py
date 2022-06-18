#Setahu saya list itu adalah sebuah variabel yang bisa menampung berbagai macam tipe data 
#Sedangkan Linked list adaalh banyaknya variabel yang dihibungkan jadi seperti rantai  

class Node:
    def __init__(self, data):
        #Untuk menyimpan atau menampung data 
        self.item = data
        #Untuk menyimpan atau menampung data selanjutnya 
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None
    
    #Method ini digunakan untuk menampilkan data  
    def traverse_list(self):
        #Jika self.star_node adalah kosong maka linked list tidak memiliki element 
        if self.start_node is None:
            print("Tidak ada element yang bisa ditampilkan")
            return
        #Dan jika tidak kosong maka akan masuk di else dan akan diproses
        #Berfungsi untuk mencetak hadil dari data yang diinputkan oleh user 
        else:
            #Membuat variabel yang menunjuk pada node paling awal 
            n = self.start_node
            #Melakukan perulangan jika data n tidak kosong 
            while n is not None:
                #Melakukan print data n 
                print(n.item , " ")
                #Merubah value n menjadi node selanjutnya 
                n = n.ref

    #Method ini berfungsi untuk memasukan nilai atau node diawal linked list 
    def insert_at_start(self, data):
        #Membuat node baru 
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node
    
    #Method ini berfungsi untuk memasukkan nilai atau node diakhir linked list 
    def insert_at_end(self, data):
        #Membuat node baru 
        new_node = Node(data)
        #Kondisikan jika kosong maka langsung ditambahkan sebagai node awal 
        if self.start_node is None:
            self.start_node = new_node
            return
        #Membuat variabel yang menunjuk pada node paling awal 
        n = self.start_node
        #Perulangan untuk mengecek berada pada node paling akhir 
        while n.ref is not None:
            n= n.ref
        n.ref = new_node 
    
    #Method ini berfungsi untuk menghapus data yang paling awal
    def delete_at_start(self):
        if self.start_node is None:
            print("Tidak ada element yang bisa dihapus")
            return
        self.start_node = self.start_node.ref

    #Method ini berfungsi untuk menghapus data yang paling akhir 
    def delete_at_end(self):
        if self.start_node is None:
            print("Tidak ada element yang bisa dihapus")
            return

        #Membuat variabel yang menunjukan node paling awal 
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    #Method yang berfungsi untuk membalikkan setiap element pada data yang diinputkan 
    def reverse(self):
        x = self.start_node
        y = None
        while x:
            ref = x.ref
            x.ref = y
            y = x
            x = ref 
            self.start_node = y

    #Method ini berfungsi untuk menampilkan element pertama pada data yang diinputkan 
    def tampilan_pertama(self):
        #Kondisi jika kosong maka langsung ditambahkan sebagai node awal
        if self.start_node is None:
            print("Tidak ada element yang bisa ditampilkan")
            return
        else:
            n = self.start_node
            return n.item
    
    def tampilan_akhir(self):
        LinkedList.reverse(self)
        #Kondisi jika kosong maka langsung ditambahkan sebagai node awal
        if self.start_node is None:
            print("Tidak ada element yang bisa ditampilkan")
            return
        else:
            n = self.start_node
            return n.item
    

#Stack adalah struktur data yang bisa menyimpan banyak data 
#Seperti array dan list 
#Stack ini seperti tumpukan jadi yang terkahir kali dimasukkan itu adalah nilai yang bisa dihapus terlebih dahulu 
#Operasi push: penambahan 1 data baru 
#Operasi pop: penghapusan 1 data 
#Stack memiliki sifat Last In First Out (LIFO) 
class Stack:
    #Method init ini bertujuan untuk menyimpan data stack yang diinputkan oleh user kedalam kelas Linkedlist()
    def __init__(self):
        self.stack = LinkedList()

    #Method push ini berfungsi untuk memasukkan data yang diinputkan oleh user ke self.stack
    def push(self, item):
        #Ini kenapa memakai insert_at_start karena data yang dimasukkan terelbih dahulu akan mengarah ke kanan atau ke yang 
        # paling dalam dari suatu variable penampung, jadi seperti data akan bergeser ke kanan 
        self.stack.insert_at_start(item)

    #Method pop ini berfungsi untuk menghapus data pada variable self.stack 
    def pop(self):
        #Ini kenapa memakai delete_at_start karena dalam method itu ada proses self.start_node = self.start_node.ref
        #Yang menandakan bahwa yang pertama kali dihapus adalah data yang paling akhir diinputkan oleh user 
        #Dan itu sesuai dengan konsep stack  
        removed = self.stack.delete_at_start()
        return removed

    #Method untuk menampilkan data 
    def tampilan(self):
        return self.stack.traverse_list()

    #Method untuk membalikkan nilai element 
    def kebalikan(self):
        return self.stack.reverse()

    #Method untuk menampilkan element pertama pada stack 
    def tampilan_1(self):
        return self.stack.tampilan_pertama()


#Queue adalah struktur data yang bisa menyimpan banyaknya data 
#Seperti array dan list 
#Queue ini seperti antrian jadi data yang pertama kali dimasukkan adalah data yang bisa dihapus atau data yang bisa dihapus pertama kali 
#Operasi queue ini bersifat First In First Out (FIFO)
# Operasi enqueue: penambahan 1 data baru 
# Operasi dequeue: penghapusan 1 data  
class Queue:
    #Method init ini bertujuan untuk menyimpan data queue yang diinputkan oleh user kedalamkelas Linkedlist()
    def __init__(self):
        self.queue = LinkedList()

    #Method enqueue berfungsi untuk memasukkan data yang diinputkan oleh user ke self.queue
    def enqueue(self, item):
        #Ini kenapa memakai insert_at_end karena user harus menginputkan data dari yang paling belakang 
        #Atau dari yang paling akhir terlebih dahulu 
        #Jadi kalau diibaratkan data inputan user akan bergeser kesebelah kiri 
        self.queue.insert_at_end(item)

    #Method dequeue berfungsi untuk mengahpus data yang diinputkan oleh user ke self.queue
    def dequeue(self):
        #Ini kenapa juga memakai delete_at_start karena di stack kita memakai insert_at_start dan di queue kita menggunakan 
        #insert_at_end dan itu semua mengarah ke satu penghapusan yaitu di start.node atau kepala linked list 
        removed = self.queue.delete_at_start()
        return removed

    #Method untuk menampilkan element pada data queue
    def tampilan(self):
        return self.queue.traverse_list()

    def tampilan_1(self):
        return self.queue.tampilan_pertama()

    def perhitungan(self):
        if self.queue.start_node is None:
            return 0
        n = self.queue.start_node
        count = 0

        while n is not None:
            count += 1
            n = n.ref
        return count

#Soal Nomer 1 
def balik_stack(kata):
    stack_1 = Stack()
    for insert in kata:
        stack_1.push(insert)
    
    print("Kata sebelum dibalik")
    stack_1.tampilan()
    print("Kata yang sudah dibalik")
    stack_1.kebalikan()
    stack_1.tampilan()

# balik_stack("shohibun")

#Soal Nomer 2 
def palindrome(kata):
    stack_1 = Stack()
    queue_1 = Queue()
    
    for insert in kata:
        stack_1.push(insert)
        queue_1.enqueue(insert)
    
    x = 1
    while x <= len(kata):
        tampilan1 = queue_1.tampilan_1()
        tampilan2 = stack_1.tampilan_1()

        if tampilan1 == tampilan2:
            awal = queue_1.dequeue()
            akhir = stack_1.pop()
        else:
            return "Bukan Palindrome"
        x += 1
    return "Palindrome"

# print(palindrome("shohibun"))

class StackQueue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, data):
        data = data.lower()
        for insert in data:
            self.queue1.enqueue(insert)

    def pop(self):
        while self.queue1.perhitungan() != 1:
            temp = self.queue1.tampilan_1()
            self.queue2.enqueue(temp)
            self.queue1.dequeue()
        else:
            self.queue1.dequeue()
        
        while self.queue2.perhitungan() != 0:
            temp = self.queue2.tampilan_1()
            self.queue1.enqueue(temp)
            self.queue2.dequeue()
    
    def tampilan_data(self):
        return self.queue1.tampilan()

data1 = StackQueue()
data1.push("hallo")
print("Data yang diinputkan:")
data1.tampilan_data()
print("Data yang telah dihapus menggunakan method pop:")
data1.pop()
data1.tampilan_data()

