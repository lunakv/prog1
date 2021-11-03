# Jednoduchá ukázka využití slovníků
# Pod každým jménem si ukládáme účetní zůstatek,
# program zůstatek vypíše pro dotázané jméno (pokud existuje)

bank = { 'Alice': 12, 'Bob': 44, 'Cecile': 100, 'Dave': 56, 'Eve': 1000 }

# Tip: běžící programy se dají zabít zkratkou Ctrl+C
while True:
    print('Enter name:')
    name = input()
    if name in bank:
        print(name, 'has a balance of', bank[name], 'CZK')
    else:
        print('Name does not have an account')




























