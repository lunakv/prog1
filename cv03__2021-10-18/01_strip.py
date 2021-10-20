# Navazuje na předchozího cvičení

# Uživatel zadá na vstupu řetězec, který může mít na začátku i konci mezery
# Program vypíše řetězec bez těchto mezer
#
# Př.: 
#          0123456789
# vstup = "   abcdef "
# vystup = "abcdef"

vstup = input()

start = 0
while vstup[start] == ' ':
    start = start+1

end = len(vstup) - 1
while vstup[end] == ' ':
    end = end - 1

##########################################################################
# print('start: ' + str(start))
# print('end: ' + str(end)) 
print(vstup[start:end+1]) # rozmyslete si proč +1



