# Třída reprezentující zásobník
class Stack:
    # inicializace
    def __init__(self):
        self.items = [] # prvky zásobníku ukládáme v poli

    # přidání prvku na konec zásobníku
    def push(self, item):
        self.items.append(item)

    # odebrání prvku z konce zásobníku 
    def pop(self):
        return self.items.pop()

    # kontrola prázdnosti zásobníku
    def is_empty(self):
        return len(self.items) == 0
    
    # pohled na poslední prvek zásobníku bez odebrání
    def peek(self):
        return self.items[-1]

s = Stack()
s.push(4)
s.push(5)
i = s.pop() # 5
print(i) 
s.push(3)
print(s.pop()) # 3
print(s.is_empty()) # False, v zásobníku je 4
print(s.pop()) # 4
print(s.is_empty()) # True
