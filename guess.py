from random import randint

won = False # variable for game ongoing / game over
goal = randint(0, 9)

while not won: # run indefinitely until game over
  guess = int(input("Guess a number between 0-9:"))
  if guess == goal:
    print("You win!")
    # clicker question: what goes here?
    won = True

# Suggestion: Give a hint about whether you went over or under. (hot...warm...tepid...chill...cold)
  # Extend the if statement for when guess < goal, guess > goal, etc.
# Suggestion: Three strikes and "You lose!"
  # Keep track of while loop runs, increase a variable.
# Suggestion: User selects the range instead of it being "hard-coded."
# Suggestion: Lose condition number. 
# Suggestion: Give a hint about whether you went close to the evil number.