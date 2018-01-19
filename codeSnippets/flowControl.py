name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

# # simple if/else statement
if age >= 18:
    print("You are old enough to vote")
else:
    print("Please come back in {0} years.".format(18 - age))

print("")

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < 5:
    print("Please guess higher")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it correctly!")
    else:
        print("Sorry, you guessed it incorrectly.")
elif guess > 5:
        print("Please guess lower")
        guess = int(input())
        if guess == 5:
            print("Well done, you guessed it correctly!")
        else:
            print("Sorry, you guessed it incorrectly.")
else:
    print("You got it right the first time.")

# modified:

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess != 5:
    if guess < 5:
        print("Please guess higher.")
    else:
        print("Please guess lower.")

    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it correctly.")
    else:
        print("Sorry, you guessed it incorrectly.")
else:
    print("You got it right the first time!")

# pt2

age = int(input("How old are you? "))

if (age >= 16) and (age <= 65):
    print("Have a good day at work!")

if 16 <= age <= 65:
    print("Have a good day at work!")

if 15 < age < 66:
    print("Have a good day at work!")

if (age < 16) or (age > 65):
    print("Enjoy your free time!")
else:
    print("Have a good day at work.")

x = input("Please enter some text ")

if x:
    print("You entered '{}'".format(x))
else:
    print("You did not enter anything")

reversed true and false
print(not False)
print(not True)

# modified
age = int(input("How old are you? "))

if not(age < 18):
    print("You are old enough to vote.")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years".format(18 - age))

# modified
parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter not in parrot:
    print("{} is wrong, bub".format(letter))
else:
    print("I don't need that letter.")