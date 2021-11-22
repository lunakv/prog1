# faktoriál - rekurzivně
def faktorial(n):
    if n == 1:
        return 1
    f = faktorial(n-1)
    return n * f

# faktoriál - bez rekurze
def faktorial2(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

def faktorial3(n):
    f = 1
    i = 1
    while i <= n:
        f = f * i
        i += 1
    return f

# fibonacciho posloupnost - rekurzivně
def fib(n):
    if n == 1 or n == 2:
        return 1
    last = fib(n-1)
    almost_last = fib(n-2)
    return last + almost_last

# fibonacciho posloupnost - bez rekurze
def fib2(n):
    if n <= 2:
        return 1

    last = 1
    prev = 1
    for i in range(n-2):
        new_last = last + prev
        prev = last
        last = new_last
    return last
