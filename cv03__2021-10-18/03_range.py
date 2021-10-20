# Máte-li seznam, vypište prvky seznamu na pozicích dělitelných dvěmi a/nebo třemi.

lst = [2, 6, "A", False, 15, 22, "text", "99"]

for i in range(len(lst)):
    if (i % 2 == 0) or (i % 3 == 0):
        print(lst[i]) 
