"""
2.06 - Game Loop
-----------------------------

Helpful Links
- https://docs.python.org/3/reference/compound_stmts.html#while
- https://www.w3schools.com/python/python_while_loops.asp
- https://en.wikipedia.org/wiki/Video_game_programming#Game_structure

Sample rock/paper/scissors game with a game loop
"""
# Import the random library to get a random number for the comptuer player
import random

# Define friendly names for the game options
play_option_names = ['rock', 'paper', 'scissors']
# Define valid user entered values
play_options = ['r', 'p', 's']
# Initialize values for game play
game_over = False
computer_score = 0
user_score = 0

# Loop until the game is over
while not game_over:
    # Get input from the user
    print("Score Computer:", computer_score, "User:", user_score)
    user_option = input(
        "Enter 'r' for rock, 'p' for paper, 's' for scissors or 'q' to quit: ")
    # If user enters q then no need to go further
    if user_option == 'q':
        game_over = True
        continue  # Skips rest of loop and goes back to while
        # You could use "break" here to just exit out of the loop

    # User wants to play so check that a valid option was entered
    # using the "in" method to ensure a valid option was entered
    elif user_option in play_options:
        # Get a random number from 0..2 for computer play
        computer_option_ndx = random.randint(0, len(play_options) - 1)
        # Use that number as an index into the chars
        computer_option = play_options[computer_option_ndx]
        print(
            'Computer played:',
            # We already have an index for the comptuer option
            play_option_names[computer_option_ndx],
            'User played:',
            # Get the name of the user option based on the letter entered
            # using .index()
            play_option_names[play_options.index(user_option)]
        )

        # Now check to see who wins
        # If computer and user pick the same its a tie
        if computer_option == user_option:
            print('Tie, both picked:', play_option_names[computer_option_ndx])

        # Otherwise check the possible options where the computer can win
        elif computer_option == 'r' and user_option == 's':
            print('Computer wins')
            computer_score += 1
        elif computer_option == 'p' and user_option == 'r':
            print('Computer wins')
            computer_score += 1
        elif computer_option == 's' and user_option == 'p':
            print('Computer wins')
            computer_score += 1

        # Computer didn't win and it wasn't a tie so user wins
        else:
            print('User wins')
            user_score += 1
    else:
        # Got here because the user didn't enter r, p, s or q
        print('You entered an invalid option:', user_option)

print('Game over')
print('Final Score Computer:', computer_score, 'User:', user_score)
