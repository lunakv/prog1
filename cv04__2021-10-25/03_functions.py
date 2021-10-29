# Definice funkce
def helloWorld():
    print('Hello world!')

# Volání funkce
helloWorld()

# Funkce může mít argumenty - tělo funkce pak pracuje s hodnotami dosazenými do argumentů
def greet(name):
    print(f'Hello {name}!') # formátovaný řetězec - ekvivalentní následujícímu řádku
    # print('Hello ' + name + '!')

# Hodnoty argumentů dosazujeme při každém volání funkce
greet('world')
greet('everyone')
greet('Karel')

print('----------')

# Funkce může po zavolání vrátit návratovou hodnotu, kterou můžeme dál využít
def power(a, b = 2):
    return a ** b

p = power(2, 3) # (hodnotu, kterou vrátí volání funkce, dosazujeme do proměnné)
print(p)
print(power(2, 3))

# Argumentům můžeme v definici přiřadit defaultní hodnotu, která se použije, pokud při volání argument nezadáme
def power2(a, b = 2)
    return a ** b

print(power2(2, 3))
print(power2(3))

# V těle funkce můžeme volat a používat návratové hodnoty jiných funkcí
def circle_area(radius):
    area = 3.14 * power(radius, 2)
    return area

print(circle_area(2))

##### Cvičné funkce #####
# Funkce `is_even(n)` vrací `True`, pokud je n sudé a `False`, pokud je n liché;
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(5))

# Napište funkci `is_odd(n)`. Využijte při tom funkci `is_even(n)`
def is_odd(n):
    return not is_even(n)

print('----------')

def ascending(l):
    for i in range(len(l) - 1):
        if l[i] > l[i+1]:
            return False
    return True

def descending(l):
    for i in range(len(l) - 1):
        if l[i] < l[i+1]:
            return False
    return True

def ordered(l):
    return ascending(l) or descending(l)
