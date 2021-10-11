## Vstup a vystup ##
x = input()
print(x)

#################################
## Promenne ##

# Cela cisla
x = 1
# Desetinna cisla
y = 1.5
# Retezce
z = "ahoj"
z = 'ahoj'
# Boolean
b = True
b = False

# Prevod mezi typy
i = int('2')
f = float('3.5')
s = str(4)

#################################
## If, while ##

x = int(input())
if x < 2:
    print('x je mensi nez dva')
elif x < 4:
    print('x je mezi dvema a ctyrmi')
elif x < 6:
    print('x je mezi ctyrmi a sesti')
else:
    print('x je vetsi nez dva')

while x > 0:
    print('x je vetsi nez nula')
    print(x)
    x = int(input())
print('x uz neni vetsi nez nula')

#################################
## Zakladni operace s cisly ##

# vypocty
1 + 2    # scitani (== 3)
2 - 3    # odcitani (== -1)
3 * 4    # nasobeni (== 12)
4 / 5    # deleni (== 0.8) !!vysledek vzdy hodnota float (desetinne cislo)!!
14 // 5  # celociselne deleni - zaokrouhluje dolu (== 2)
7 % 3    # zbytek po deleni (== 1)
2 ** 4   # umocnovani (== 16)

# porovnavani (vysledkem hodnota boolean)
x == 42      # rovnost !!potreba dve rovnitka - jedno znamena prirazeni!!
x != 42      # nerovnost
x < 42       # mensi nez
x > 42       # vetsi nez
x <= 42      # mensi nebo rovno
x >= 42      # vetsi nebo rovno

#################################
## Zakladni operace s retezci ##
s = 'abcdefghijklmnop'

s[2]           # vyber konkretniho znaku (== 'c') !!indexujeme vzdy od 0!!
s + 'qrst' # slepovani retezcu (== 'abcdefghijklmnopqrst')
'ab'*3         # "exploze" retezce (== 'ababab')
s == 'xyz'     # porovnani na rovnost hodnoty (== False)
s != 'xyz'     # porovnani na nerovnost hodnoty (== True)
s < 'xyz'      # porovnani podle lexikografickeho usporadani (== True) !!pozor na vicejazycne srovnavani (viz. prednaska)!!
len(s)         # delka retezce (== 6) !!cislujeme od 0 - posledni znak je na indexu len(s)-1!!

# s + 3 !!Nelze!! (program spadne - snazime se secist retezec a cislo)
