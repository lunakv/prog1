# Třída reprezentující haldu
class Heap:
    # inicializace prázdné haldy
    def __init__(self):
        self.__items = []
    
    # přidání prvku do haldy
    def insert(self, value):
        # přidáme prvek na konec
        self.__items.append(value)

        # probubláváme se nahoru 
        i = len(self.__items) - 1
        while i != 0:
            p_i = self.__parent(i)
            # pokud je otec menší než prvek, bublání končí
            if self.__items[p_i] <= self.__items[i]:
                break

            # jinak prohodíme prvek s otcem 
            tmp = self.__items[p_i]
            self.__items[p_i] = self.__items[i]
            self.__items[i] = tmp
            # a pokračujeme
            i = p_i

    # Implementace jako DÚ 
    # (doporučuji konzultovat přednášku, případně Průvodce labirintem Algoritmů)
    # def extract_min(self):

    ## Pomocné funkce, pro zadaný index vracejí index levého, resp. pravého syna a rodiče
    # (pozor: funkce nejsou ošetřené proti případům, kdy otec/synové neexistují)

    def __left(self, i):
        return 2*i + 1

    def __right(self, i):
        return 2*i + 2

    def __parent(self, i):
        return (n-1)//2


h = Heap()
h.insert(15)
h.insert(5)
print(h.extract_min()) # 5
