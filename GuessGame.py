import random

number =  random.randint(1, 10)
tries = 1

uname = input("Hello, What is your name?")
print("Hello,", uname + ".")

question = input("Would you like to play a game? [Y/N]")
if question == "n" or question == "N":
    print("Ohh.. its ok..!")

if question == "y" or question == "Y":
    print("I'm thinking a number between 1 to 10")
    guess = int(input("Have a guess: "))
    if guess > number:
        print("Guess lower...")
    if guess < number:
        print("Guess higher...")
    while guess != number:
        tries += 1
        guess = int(input("Try again..."))
        if guess > number:
            print("Guess lower...")
        if guess < number:
            print("Guess higher...")
        if guess == number:
            print("Yes..Well done..You win..!", uname, "in only", tries, "tries.")
            print("The number was", number,".")