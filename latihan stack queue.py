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
        data = self.start_node.item
        self.start_node = self.start_node.ref
        return print(data)       

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
            return print ("0")
        n = self.start_node
        count = 0;
        while n is not None:
            count = count + 1
            n = n.ref
        return print ("Jumlah elemen adalah :",count)

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

class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, item):
        self.stack.insert_at_start(item)

    def pop(self):
        removed = self.stack.delete_at_start()
        return removed
    
    def peek(self):
        if self.stack.start_node is None:
            print("Stack has no element")
            return
        else:
            n = self.stack.start_node
            print("Item teratas adalah :", n.item )

    def peek_all(self):
        return self.stack.traverse_list()

    def count(self):
        return self.stack.get_count()

class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, item):
        self.queue.insert_at_end(item)

    def dequeue(self):
        removed = self.queue.delete_at_start()
        return removed

    def peek(self):
        if self.queue.start_node is None:
            print("Queue has no element")
            return
        else:
            n = self.queue.start_node
            print("Item teratas adalah :", n.item )

    def peek_all(self):
        return self.queue.traverse_list()
    
    def count(self):
        return self.queue.get_count()

                        ### LATIHAN SOAL ###
### Tambahkan method peek untuk melihat (tanpa menghapus) bagian top stack


### Tambahkan method count untuk menghitung banyaknya elemen queue


### Implementasikan push dan pop pada stack


### Implementasikan enqueue dan dequeue pada queue
