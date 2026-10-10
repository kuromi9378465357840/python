import random
number = random.randint(1,1000)
attempts = 0
while True:
    guess = int(input("Guess a number between 1 and 1000: "))
    attempts += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it in", attempts, "attempts!")
        break
