from random import randint
import sys


# Generate a random number
answer = randint(int(sys.argv[1]), int(sys.argv[2]))

# Check the guess
while True:
    # Get input from user
    guess = int(input('Guess a number 1-10 ')) 
    try:
        if int(sys.argv[1]) < guess < int(sys.argv[2]):
            if guess == answer:
                print('You are a genius')
                break
        else:
            print(f'Hey bozoo, i said {int(sys.argv[1])}-{int(sys.argv[2])}!')
    except ValueError:
        print("Invalid input, please enter a number")
        continue  