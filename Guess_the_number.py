import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between 1 to {x}: "))
        if guess > random_number:
            print("Sorry! Try again, Number is too high")
        elif guess< random_number:
            print("Sorry! Try again, Number is too low")
    print(f"Yay! You have guessed {random_number} correctly")




guess(20)
