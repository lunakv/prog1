import os

# absolutní cesty k souborům
input_file = os.path.dirname(os.path.realpath(__file__)) + "/input.txt"
output_file = os.path.dirname(os.path.realpath(__file__)) + "/output.txt"

# čtení první řádky souboru
f = open(input_file, "r")
print(f.readline())
f.close()

# čtení první řádky souboru - with syntax
with open("input.txt", "r") as f:
    print(f.readline())

# čtení všech řádek souboru do pole
with open("input.txt", "r") as f:
    print(f.readlines())

# čtení všech řádek souboru po jedné - while
with open("input.txt", "r") as f:
    l = f.readline()
    while l != "":
        print(l, end='')
        l = f.readline()

# čtení všech řádek souboru po jedné - for
with open("input.txt", "r") as f:
    for l in f:
        print(repr(l))

# zápis do souboru - vytvoří/přepíše soubor
with open("output.txt", "w") as f:
    f.write("abcd\n") # "\n" v řetězci reprezentuje konec řádku
    f.write("efgh")

# zápis do souboru - append
with open("output.txt", "a") as f:
    f.write("ijkl\n")
    f.write("mnop")

# Příklad - zkopírování souboru
i = open("input.txt", "r")
o = open("output.txt", "w")
for line in i:
    o.write(line)
i.close()
o.close()
