
def skoky_kone_z(x, y):
    '''Vrátí všechny pozice, na které umí skočit jedním skokem kůň z (x,y)'''
    # Jak umí skákat kůň
    skoky = [(+2, +1), (+2, -1), (+1, +2), (+1, -2), (-2, +1), (-2, -1), (-1, +2), (-1, -2)]
    # Dosažitelná pole
    cile = []
    for dx, dy in skoky:
        nove_x = x + dx
        nove_y = y + dy
        if 0 <= nove_x < 8 and 0 <= nove_y < 8:
            # nesmíme vyskočit mimo šachovnici
            cile.append((nove_x, nove_y))

    return cile


def delka_konem(start_x, start_y, cil_x, cil_y):
    '''Najde nejmenší počet skoků na cestu koněm z (start_x, start_y) do (cil_x, cil_y)'''
    # Řádky/sloupce šachovnice číslujeme 0..7
    fronta = []
    objevene = set()
    objevene.add((start_x, start_y))
    fronta.append((start_x, start_y, 0))

    while len(fronta) > 0:
        x, y, skoky = fronta.pop(0)
        if x == cil_x and y == cil_y:
            return skoky

        for nove_x, nove_y in skoky_kone_z(x, y):
            if (nove_x, nove_y) not in objevene:
                objevene.add((nove_x, nove_y))
                fronta.append((nove_x, nove_y, skoky+1))


# Ukázkové testy
print('Délka z (0,0) do (1,2):', delka_konem(0,0, 1,2))
print('Délka z (0,0) do (0,1):', delka_konem(0,0, 0,1))
print('Délka z (1,3) do (7,7):', delka_konem(1,3, 7,7))
print('Délka z (7,7) do (1,3):', delka_konem(7,7, 1,3))
