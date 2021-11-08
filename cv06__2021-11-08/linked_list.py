# Třída pro jeden prvek spojového seznamu
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

# ruční vytváření seznamu po prvcích
p1 = Node(10, None)
p2 = Node(1, p1)
p3 = Node(3, p2)
p4 = Node(6, p3)
p5 = Node(5, p4)

# p5 -> p4 -> p3 -> p2 -> p1 -> None

# Dostane prvek, vypíše hodnoty seznamu od tohoto prvku až do konce
def print_list(node):
    while node != None:
        print(node.value, end=' ')
        node = node.next
    print()

print_list(p5) # 5 6 3 1 10
print_list(p2) # 1 10
print_list(4)
print_list(None) #

{[}]
