import random 




    if user == computer: 
        return 'tie'
    if is_win(user, computer):
        return 'You won!'
    return 'You loose!'

def is_win(player, opponent):
   # r>s, s>p, p>r 
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())


