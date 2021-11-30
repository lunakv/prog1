"""
Vypište (rekurzivně) všechny posloupnosti 
znaků "+" a "-" délky N.

Tedy pro N = 3 to jsou:
    ---
    --+
    -+-
    -++
    atd...


Řešení:
rekurzivní funkce vracející seznam všech
posloupností délky N.
"""

def f(n):
    if n == 1:
        return ["+", "-"]
    
    seqs = []
    subseqs = f(n-1)

    for s in subseqs:
        seqs.append(s + "+")
        seqs.append(s + "-")
    
    return seqs

for seq in f(4):
    print(seq)
