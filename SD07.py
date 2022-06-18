class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None
    
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n= n.ref
        n.ref = new_node;
    
    def insert_after_item(self, x, data):
        n = self.start_node
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no element")
            return

        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Index out of bound")
        else: 
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        self.start_node = self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def get_count(self):
        if self.start_node is None:
            return 0;
        n = self.start_node
        count = 0;
        while n is not None:
            count = count + 1
            n = n.ref
        return count

    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("item not found")
        return False

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        # Deleting first node
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return

        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref = n.ref.ref

                            ### SOAL TUGAS ###
### Buatlah method untuk mencari banyaknya anggota sebuah linked list
    def Banyak_Anggota(self):
        if self.start_node is None:
            return

        n = self.start_node
        Banyak = 0
        while n is not None:
            Banyak += 1
            n = n.ref
        return Banyak

### Buatlah method untuk menghitung jumlah (sum) semua bilangan di sebuah linked list
    def Jumlah(self):
        if self.start_node is None:
            return

        Jumlah = 0
        n = self.start_node
        while n is not None:
            Jumlah += n.item
            n = n.ref
        return Jumlah 

### Buatlah method untuk menyambung dua buah linked list menjadi sebuah linked list. 
### Pengguna bisa menetukan susunannya apakah linkedlist1linkedlist2 atau linkedlist2linkedlist1
    def Sambung(self, linked_list2):
        n = self.start_node
        m = linked_list2.start_node
        while n is not None:
            n.insert_at_end(m.item)
            n = n.ref
        return n

### Buatlah method untuk menambahkan data ke linkedlist sedemikian hingga data 
### yang ada di linkedlist dalam kondisi terurut
    def Urut(self):
        n = self.start_node
        while n is not None:
            m = n.ref
            while m is not None :
                if n.item > m.item:
                    n.item, m.item = m.item, n.item
                n = n.ref
            return n.item

### Buatlah method untuk membalik arah semua pointer di linkedlist
    def Membalik(self) :
        n = self.start_node
        m = None
        while n:
            ref = n.ref
            n.ref = m
            m = n
            n = ref
            self.start_node = m
