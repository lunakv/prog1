# Definice třídy pro komplexní čísla
class Complex:
    # Každá funkce třídy má první parametr self, který obsahuje vždy objekt,
    # na kterém se funkce volá

    # Speciální funkce __init__ se zavolá vždy při vytvoření nového objektu
    def __init__(self, real, imag):
        # V objektu můžou být uložená data (podobně jako ve slovníku)
        self.re = real
        self.im = imag
    
    # Funkce vypisující pěkně hodnoty uložené v objektu
    def write(self):
        print('re:', self.re, 'im:', self.im)

    # Funkce na kontrolu rovnosti s jiným komplexním číslem 
    def is_equal(self, other):
        if self.re == other.re and self.im == other.im:
            return True
        else:
            return False
   
    # Funkce vracející velikost komplexního čísla
    def size(self):
        return (self.re ** 2 + self.im ** 2) ** (1/2)

    # Funkce, která vynásobí toto komplexní číslo reálným číslem
    def multiply_by(self, number):
        self.re *= number
        self.im *= number

####################################

# Nový objekt vytvoříme pomocí názvu třídy a případně parameterů funkce __init__ (za self)
z = Complex(13, 22)
z2 = Complex(15, 7)
# z = Complex() # pokud bychom na třídě funkci __init__ nedefinovali, nebo by neměla parametry mimo self

# Můžeme přistupovat k datům uloženým v daném objektu
x = z.re
print(z.im)
z.re = 4

# Můžeme na objektu volat funkce definované v jeho třídě
z.multiply_by(3) # parametr self se doplní automaticky podle toho, na jakém objektu funkci voláme (z). Ostatní uvádíme jako u běžných funkcí
z.write() # funkce write nemá parametry mimo self, tak žádné nedodáváme (proč používáme speciální funkci? vyzkoušejte si, co udělá 'print(z)')
print(z.size())

z3 = Complex(15, 7)
if z2.is_equal(z3):
    # Tato řádka se vypíše (v z2 i z3 jsou uložené stejné hodnoty)
    print('Yay!')

if z2 == z3:
    # !! Tato řádka se nevypíše !! 
    # Operátor == na objektech srovnává, zda je v obou proměnných uložený tentýž objekt
    # z2 a z3 obsahují různé objekty (přestože se stejnými hodnotami), tudíž test na rovnost vrátí False
    print('Nay!')

z4 = z2
if z2 == z4:
    # Tato řádka se vypíše
    # Do z4 jsme uložili odkaz na stejný objekt jako je v z2, tudíž obsahují tentýž objekt
    # (viz. operátor 'is' z přednášky a povídání o ukládání odkazů v proměnných z minulého cvičení)
    print('Yay!')

z4.re = 6
z4.write()
z2.write() # !! Obě proměnné ukazují na stejný objekt !!









z2.write()
