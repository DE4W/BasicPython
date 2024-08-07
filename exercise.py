for count in range(101):
    if(count == 0):
        continue
    if(count %2 == 0):
        print(count, "is even")
    else:
        print(count, "is odd")
        if(count == 101):
            break

import random
num = random.randint(1, 100)

guess = -1
attempts = 0

while num != guess:
    guess_str = input("Guess the number: ")
    guess = int(guess_str)
    attempts += 1
    if(num < guess):
        print("The guess is too high, try again!")
    if(num > guess):
        print("The guess is too low, try again!")
        
print(f"Congratulation, the guess is correct! You took {attempts} attempts to guess it correctly!")