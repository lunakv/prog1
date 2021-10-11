# Uživatel zadává po řádcích čísla, dokud nezadá prázdný řádek (Enter)
# Program vypíše aritmetický průměr zadaných čísel
# Př.:
#
# 1
# 3
# 15
# 9 
#
# Aritmeticky prumer je: 7

soucet = 0
pocet = 0

vstup = input()
while vstup != "":
    n = int(vstup)
    soucet = soucet + n
    pocet = pocet + 1
    vstup = input()

prumer = soucet / pocet
print('Pocet cisel je: ' + str(pocet))
print('Soucet cisel je: ' + str(soucet))
print('Aritmeticky prumer je: ' + str(prumer))
