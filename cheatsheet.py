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
# Seznamy
s = []
s = [1, 2, 3]

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
## For, range() ##

for i in [1,2,3,4,5]:
    print(i)

for character in "qwertyuiop":
    print(character)

for i in range(1, 6): # !!cislo 6 uz v cyklu nebude!!
    print(i)

for i in range(10): # == range(0, 10)
    print(i)

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
s + 'qrst'     # slepovani retezcu (== 'abcdefghijklmnopqrst')
# s + 3 !!Nelze!! (program spadne - snazime se secist retezec a cislo)
'ab'*3         # "exploze" retezce (== 'ababab')
s == 'xyz'     # porovnani na rovnost hodnoty (== False)
s != 'xyz'     # porovnani na nerovnost hodnoty (== True)
s < 'xyz'      # porovnani podle lexikografickeho usporadani (== True) !!pozor na vicejazycne srovnavani (viz. prednaska)!!
len(s)         # delka retezce (== 6) !!cislujeme od 0 - posledni znak je na indexu len(s)-1!!

# Slicing
s[2:6]         # slice od druheho do sesteho znaku (== 'cdef') !!pocatecni index patri do slicu, koncovy uz ne!!
s[12:]         # chybi druhy index - implicitne do konce retezce (== 'mnop')
s[:4]          # chybi prvni index - implicitne od zacatku retezce (== 'abcd')
s[10:-2]       # zaporne indexy - pocitano od konce (posledni znak index -1) (== 'klmn')
s[-4:]         # (== 'mnop')
s[3:9:2]       # treti parametr udava delku kroku mezi znaky (== 'dfh')
s[8:3:-1]      # zapornym skokem prochazime string pozpatku (== 'ihgfe') !!zde vyssi index prvni!!

s[::-1]        # cely retezec pozpatku - zacatek i konec jsou implicitne okraje retezce, krok -1 znamena pruchod od konce

#################################
## Zakladni operace se seznamy ##
l = [5, 10, 15, 20, 25, 30]

l[0]             # vyber konkretniho prvku (== 5)
l[1:4]           # slicing - stejne jako u retezcu (== [10, 15, 20])
len(l)           # delka seznamu (== 6)
# l[99]          # !!program spadne - nelze brat prvek z pozice >= delce seznamu!!

l.append(35)     # pridani prvku na konec seznamu
x = l.pop()      # odstraneni prvku z konce seznamu (vraci odebranou hodnotu)
l.insert(2, 'a') # prida 'a' do seznamu na pozici 2 (prvky pozice 2+ se posunou doprava)

l2 = l
l.append(40)     # !! l i l2 obsahuji stejny seznam! zmena se projevi i v l2!!
