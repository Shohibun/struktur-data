class Node:
    def _init_(self, value):
        self.value = value
        self.next = None

class Stack:
    def _init_(self):
        self.head = Node("head")
        self.size = 0


    def masuk(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    
    def keluar(self):
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

if __name__ == "__main__":
    kata = "malam"
    kata_2 = ""
    stack = Stack()
    for i in kata:
        stack.masuk(i)

    for _ in kata:
        kata_2 += stack.keluar()
    
    if kata == kata_2:
        print("palindrome")