import random

def play():
    user = input("'R' for Rock,'P' for Paper, 'S' for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie' 
    
    if is_win(user, computer):
        return 'You won!'
    return 'You lost'


def is_win(player, opponent):
    if (player == 'r'and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print(play())    