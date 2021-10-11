# Uživatel zadá na vstupu řetězec, který může mít na začátku i konci mezery
# Program najde index prvního a posledního znaku na vstupu, který není mezera
#
# Př.: 
#          0123456789
# vstup = "   abcdef "
# start = 3
# end = 8

vstup = input()

start = 0
while vstup[start] == ' ':
    start = start+1

end = len(vstup) - 1
while vstup[end] == ' ':
    end = end - 1

print('start: ' + str(start))
print('end: ' + str(end)) 
    


