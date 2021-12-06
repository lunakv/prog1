"""
Kolik existuje binárních stromů na N vrcholech?

Řešení: rekurzivně podle počtu vrcholů v synech
Pro všechny možnosti rekurzivně spočítáme počet podstromů
"""

def c(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    total = 0
    for i in range(n):
        total += c(i) * c(n-1-i)
    return total


# Výsledky pro i=0..9
for i in range(10):
    print(c(i))
