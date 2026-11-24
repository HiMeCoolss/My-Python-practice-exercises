import random

def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return 'not valid'

def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'

def rpsls(player_choice):
    player_number = name_to_number(player_choice)
    print('Player chooses' + ' ' + player_choice)
    if player_number == 'not valid':
        print('Error: Not a valid option.')

    else:
        comp_number = random.randrange(0, 5)
        comp_choice = number_to_name(comp_number)
        print('Computer chooses' + ' ' + comp_choice)

        if ((comp_number - player_number) % 5 == 1
            or (comp_number - player_number) % 5 == 2):
            print ("Computer wins!")
        elif (comp_number - player_number) % 5 == 0:
            print("Player and computer tie!")
        else: 
            print("Player wins!")
    print('')

rpsls("rock")
rpsls('Spock')
rpsls('paper')
rpsls('lizard')
rpsls('scissors')
rpsls('car')