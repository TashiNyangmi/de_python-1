# exercise 6
def is_palindrome(input_string):

    clean_string = "".join([char.lower().replace(" ", '') for char in input_string])
    return (clean_string == clean_string[-1::-1])


# exercise 7
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[elem for elem in a if elem % 2 == 0]





# exercise 8


def get_valid_input(player_name = ''):
    while True:
        selection = input(f"{player_name}| select rock (r), paper(p) or scissor (s)")
        if selection in ['r', 'p', 's']:
            break
    return selection


def play_game(): 
    selection1 = get_valid_input("Player 1")
    selection2 = get_valid_input("Player 2")

    winning_combinations = [('r', 's'), ('s','p'), ('p','r')]

    if selection1 == selection2:
        print("It's a tie!")
    elif (selection1, selection2) in winning_combinations:
        print("Player 1 wins")
    else:
        print("Player 2 wins")

while True:
    play_game()
    
    if input('Do you want to play another game [y/n]?') == 'n': 
        print("Bye!!!")
        break