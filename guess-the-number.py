import time 
import random

target_number = random.randint(1,100)

print("The number between 1 and 100 was selected..Guess it!")

time.sleep(0.5) # Wait before the game start.

guess_right = 0

while True:
    guess = int(input("Enter your guess: "))
    
    guess_right += 1


    if (guess < target_number):
        time.sleep(0.2)
        print("Wrong! Guess higher....")

    elif (guess > target_number):
        time.sleep(0.2)
        print("Wrong! Guess lower....")

    else:
        time.sleep(0.2)
        print(f"Correct!! You found the {target_number}, within {guess_right} guesses!..")
        break