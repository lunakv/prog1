# Vytvořte program, který načte od uživatele celé číslo N a vypíše všechny druhé mocniny
# čísel od 1 do N.
#
# Př.:
# Vstup: 4
# Výstup:
# 1
# 4
# 9
# 16

n = int(input())
for i in range(1, n+1):
    print(i**2)