# Určete, zda posloupnost N čísel obsahuje 
# nějakou hodnotu s více než N/2 výskýty
# a pokud ano, kterou

p1 = [1, 1, 0, 0, 5, 4, 3] # return None
p2 = [0, 1, 0, 1, 1, 4, 1] # return 1


def vice_nez_pul(posloupnost):
	# Ukládáme si počty výskytů pomocí slovníku
	pocty_vyskytu = {}
	for cislo in posloupnost:
		# Pokud objevené číslo ještě ve slovníku není, přidáme ho
		# (jinak by následující řádka shodila program)
		if cislo not in pocty_vyskytu:
			pocty_vyskytu[cislo] = 0
		# a zýšíme hodnotu pod daným číslem o 1
		pocty_vyskytu[cislo] += 1
	
	# Po načtení všech výskytů postupně projdeme všechna objevená čísla z posloupnosti
	for cislo in pocty_vyskytu:
		# Pokud se nějaké vyskytuje více než N/2-krát, rovnou ho vrátíme
		# (uvědomme si, že takové číslo může být nejvýš jedno)
		if pocty_vyskytu[cislo] > len(posloupnost) // 2:
			 return cislo

	# Pokud jsme po průchodu žádné číslo nevrátili, neexistuje, tudíž vrátíme None
	return None

print(vice_nez_pul(p1))
print(vice_nez_pul(p2))
