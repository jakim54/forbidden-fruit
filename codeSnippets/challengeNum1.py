# Write a small program to ask for a name an age.
# When both values have been entered, check if the person is the right age to go on an 18 ~ 30 holiday.
# They must be over 18, but under 31.

name = input("Your name please: ")
age = int(input("Age as well: "))
# age = int(input("Age, {0}? ").format(name))

# my solution
if (age > 17) and not(age > 31):
    print("Welcome, {0}. Your age, {1}, checks out.".format(name, age))
    print("The party is just through the door.")
else:
    print("Would you kindly fuck off?")

# master solution
name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))

# if 18 <= age < 31:
if age >= 18 and age < 31:
    print("Welcome to the club, {0}".format(name))
else:
    print("Please come back later.")