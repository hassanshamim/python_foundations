from random import choice

MOVES = 'rock paper scissors'.split()
COMMANDS = {val[0] : val for val in MOVES}
COMPARISONS = { # (mine, computers): Result
               ('rock', 'rock'): "It's a tie",
               ('paper', 'paper'): "It's a tie",
               ('scissors', 'scissors'): "It's a tie",
               ('rock', 'scissors'): 'You Win!',
               ('scissors', 'paper'): 'You Win!',
               ('paper', 'rock'): 'You Win!',
               ('scissors', 'rock',): 'You lose :(',
               ('paper', 'scissors',): 'You lose :(',
               ('rock', 'paper',): 'You lose :(',
               }

def get_user_input():
    while True:
        print('Pick a move:')
        for cmd, move in COMMANDS.items():
            print(cmd + ':', move)

        user_input = input().lower()

        if user_input in COMMANDS: # it's valid
            return COMMANDS[user_input]
        else:
            print('Invalid command, try again.')


if __name__ == '__main__':
    print('Welcome to Rock Paper Scissors')
    while True:
        user_move = get_user_input()
        computer_move = choice(MOVES)

        result = COMPARISONS[(user_move, computer_move)]
        print('Computer chooses', computer_move.upper())
        print(result)
        print('-' * 30)

        replay = input('Would you like to play again? (y/n)')
        if not replay.startswith('y'):
            break
