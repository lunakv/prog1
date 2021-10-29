# Rozdělení kódu na části za použití funkcí - hra Nim
# viz. "programování shora" z přednášky

# Funkce vypíše aktuální stav hry
def print_game_state(p, rem):
    print('-------')
    print('Player ' + p + "'s turn")
    print(rem, 'coins remaining')

# Funkce načte korektní vstup od hráče
def get_player_input(rem):
    rem = min(rem, 3)
    while True:
        n = int(input('Choose a number between 1 and ' + rem))
        if n >= 1 and n <= rem:
            return n

# Funkce vrátí následujícího hráče
def next_player(p):
    if p == 'A':
        return 'B'
    else:
        return 'A'


####### Samotná hra #######
remaining = 15
player = 'A'

while remaning > 0:
    print_game_state(player, remaining)
    remaining -= get_player_input(remaining)
    if remaining == 0:
        print('Player', player, 'won the game!')
    else:
        player = next_player(player)

