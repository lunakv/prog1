# Převrácená posloupnost
#
# Vstup: Po řádcích posloupnost čísel, ukončená prázdným řádkem
# Výstup: Posloupnost vypsaná v opačném pořadí.
#
# Př.:
# Vstup:
# 1
# 3
# 5
# 9
#
# Výstup:
# 9
# 5
# 3
# 1

seznam = []

vstup = input()
while vstup != '':
    seznam.append(int(vstup))
    vstup = input()

# Varianta 1
i = len(seznam)-1
while i >= 0:
    print(seznam[i])
    i -= 1

print('--------')

# Varianta 2
for i in range(len(seznam)):
	print(seznam[len(seznam)-1-i]) # rozmyslete si proč je tu -1 potřeba

print('--------')

# Varianta 3
seznam.reverse() # list uložený v proměnné seznam se převrátí
for item in seznam:
    print(item)
