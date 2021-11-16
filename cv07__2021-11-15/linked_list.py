# Jeden uzel spojového seznamu
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

# Spojový seznam
class LinkedList:
    def __init__(self):
        self.head = None # stačí si pamantovat hlavu seznamu

    # přidání prvku na začátek seznamu
    def add_head(self, value):
        node = Node(value, self.head)
        self.head = node

    # odebrání prvku ze začátku seznamu
    def remove_head(self):
        val = self.head.value
        self.head = self.head.next
        return val

    # přidání prvku na konec seznamu
    def append(self, value):
        if self.head is None:
            self.head = Node(value, None)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(value, None)

    # odebrání prvku z konce seznamu
    def pop(self):
        node = self.head
        if node is None:
            return None
        elif node.next is None:
            val = node.value
            self.head = None
            return val
        else:
            while node.next.next is not None:
                node = node.next
            val = node.next.value
            node.next = None
            return val
    
    # přidání prvku na uvedenou pozici v seznamu
    def insert(self, val, pos):
        if pos == 0:
            new_node = Node(val, self.head)
            self.head = new_node
        else:
            i = 0
            node = self.head
            while i < pos-1:
                i += 1
                node = node.next

            new_node = Node(val, node.next)
            node.next = new_node 

    # vypsání všech prvků v seznamu
    def print_list(self):
        node = self.head
        while node != None:
            print(node.value, end=' ')
            node = node.next
        print()

### Příklady použití ###
l = LinkedList()
l.add_head(10)
l.add_head(5)
l.append(20)
x = l.remove_head()
y = l.pop()
l.insert(30, 1)
l.insert(6, 0)
l.print_list()
