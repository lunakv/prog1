'''
Spočtěte ciferný součet čísla
Vytvořte rekurzivní řešení i řešení bez použití rekurze

Př.: 1578 -> 21
'''


# Rekurzivní řešení
def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(n//10)

# Řešení bez rekurze
def digit_sum2(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum


print(digit_sum(12345))
print(digit_sum2(12345))
