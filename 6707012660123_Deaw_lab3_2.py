import random #import random value
num = random.randint(1, 100)

guess = -1
attempts = 0 #tracks the number of attempts

while num != guess: #ask for input
    guess_str = input("Guess the number: ")
    guess = int(guess_str)
    attempts += 1
    #condition
    if(num < guess):
        print("The guess is too high, try again.")
    elif(num > guess):
        print("The guess is too low, try again.")

print(f"Congratulation, the guess is correct! You took {attempts} attempts to guess it correctly!")