"""
Vytvořte funkci řešící problém Hanojských věží.

Pro velikost věže N vypíše funkce seznam instrukcí,
jak přesouvat disky mezi tyčemi, např.:

Presun z 1 na 3
Presun z 1 na 2
Presun z 3 na 2
Presun z 1 na 3
...

aby se celá věž přesunula z první tyče na druhou.


Řešení:
přesunout rekurzivně všechny disky krom posledního
na volnou tyč, následně přesunout poslední disk na 
cílovou tyč a poté rekurzivně přesunout všechny disky
na cílovou tyč
"""

def volna_vez(start, cil):
    for i in [1, 2, 3]:
        if i != start and i != cil:
            return i

def hanoi(n, start=1, cil=2):
    if n == 1:
        print("Presun z", start, "na", cil)
        return 
    
    volna = volna_vez(start, cil)
    hanoi(n-1, start, volna)
    hanoi(1, start, cil)
    hanoi(n-1, volna, cil)

hanoi(5)
