'''
Najděte anagramy.

Vytvořte funkci, která dostane slovo a vrátí seznam všech anagramů daného slova, tj. všech slov vzniklých přeuspořádáním písmen.
'''

def anagrams(word):
    if len(word) == 1:
        return [word]
    
    perms = []
    for i in range(len(word)):
        new_word = word[:i] + word[i+1:]
        sub_perms = anagrams(new_word)
        for j in range(len(sub_perms)):
            perms.append(word[i] + sub_perms[j])

    return perms


print(anagrams('abc'))
print(anagrams('bac'))
print(anagrams('a'))
print(anagrams('aaa'))
