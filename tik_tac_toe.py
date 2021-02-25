import random

winner = False
user_symbol = 'X'
ai_symbol = 'O'

row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

filled_positions = []

def user_x_or_o():
    while True:
        x_or_o = input("Do you want to be X or O? ")

        if x_or_o.lower() == 'x':
            return 'x'
        elif x_or_o.lower() == 'o':
            return 'o'
        else:
            print('You did not choose X or O please try again')

def ai_x_or_o():
    if user_symbol == 'x':
        return 'o'
    else:
        return 'x'

def print_board(row1,row2,row3):
    print()
    print(f"{row1[0]} | {row1[1]} | {row1[2]}")
    print("--|---|--")
    print(f"{row2[0]} | {row2[1]} | {row2[2]}")
    print("--|---|--")
    print(f"{row3[0]} | {row3[1]} | {row3[2]}")
    print()

def user_choice():
    while True:
        choice = input(f"Which position from 1-9 would you like to place your {user_symbol} in? ")

        if choice.isdigit():
            if int(choice) in range(1,10):
                if not int(choice) in filled_positions: 
                    filled_positions.append(int(choice))
                    return int(choice)
                elif int(choice) in filled_positions:
                    print("That position is full please type in another position")
            else:        
                print("You chose a number outside of 1-9. Please try again")

        if not choice.isdigit():
            print("You wrote a string please type in a digit from 1 - 9")

def ai_choice():
    while True:
        choice = random.randint(1,9)
        if not choice in filled_positions:
            filled_positions.append(choice)
            return choice

def update_board(position,symbol):

    if position <=3:
        row1[position-1] = symbol
    elif position > 3 and position < 7:
        row2[position-4] = symbol
    elif position >=7 and position <= 9:
        row3[position-7] = symbol

def game_logic(row1 = row1,row2 = row2,row3 = row3):

    def winner(row = row1):
        print(f"{row[i]} is the Winner!")
        winner = True
        return True

    for i in range(len(row1)):
        if row1[i] == 'x' or row1[i] == 'o':
            if row1[i] == row2[i] == row3[i]:
                return winner() #vertical
    
    for i in range(len(row1)-2):
        if row1[i] == 'x' or row1[i] == 'o':
            if row1[i] == row2[i+1] == row3[i+2]:
                return winner() #diagonal
            if row1[i] == row1[i+1] == row1[i+2]:
                return winner() #horizontal
        elif row2[i] == 'x' or row2[i] == 'o':
            if row2[i] == row2[i+1] == row2[i+2]:
                return winner() #horizontal
        elif row3[i] == 'x' or row3[i] == 'o':
            if row3[i] == row3[i+1] == row3[i+2]:
                return winner() #horizontal
        if row1[i+2] == 'x' or row1[i+2] == 'o':
            if row1[i+2] == row2[i+1] == row3[i]:
                return winner(row3) #diagonal     
    return False

def play_game():
    
    def game_check():
        if game_logic(row1,row2,row3) == True or len(filled_positions) == 9:
            return True

    while len(filled_positions) <= 9:

        print_board(row1,row2,row3)
        update_board(user_choice(), user_symbol)
        if game_check(): break

        update_board(ai_choice(), ai_symbol)   
        if game_check(): break
    
    if winner == False and len(filled_positions) == 9:
        print("You tied!")

    print_board(row1,row2,row3)

user_symbol = user_x_or_o()
ai_symbol = ai_x_or_o()
play_game()

#is symbol assignment instead of having ai_sybol we can return both user and ai in user_x_or_o
#then tuple unpack to assign
#user_syumbol, ai_symbol = user_x_or_o()

#instead of if row[i] == 'x' or 'o' you can do row1[i] == row2[i] == row3[i] == ('x' or 'o')























