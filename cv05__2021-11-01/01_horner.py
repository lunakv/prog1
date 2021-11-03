# Funkce na převod z dvojkové do desítkové soustavy a zpět
# za pomoci Hornerova schématu
#
# K rozmyšlení: jak byste funkce upravili, aby převáděly
# místo dvojkové mezi desítkovou a libovolnou číselnou soustavou?
# (pro zjednodušení 1-10)


def int_to_bin(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n //= 2
    return b

def bin_to_int(b):
    n = 0
    for digit in b:
        n *= 2
        if digit == '1':
            n += 1
    return n

print(int_to_bin(42))
print(bin_to_int('100101'))


# Funkce na převrácení čísla pomocí Hornerova schématu
def reverse(num):
    rev = 0
    while num > 0:
        rev *= 10 # reverz posuneme o číslici doleva
        rev += num % 10 # na nové poslední místo přilepíme poslední číslici z pův. čísla
        num //= 10 # z pův. čísla smažeme poslední číslici

    return rev
