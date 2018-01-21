# to run a python file in the console, simply type:
# python3 path/to/file/andNameOfFile.py

print('Greetings, Programs!')
print("Greetings, Programs!")
print('''Greetings, Programs!''')
print("""Greetings, Programs!""")
print('')
print('''Greetings,\nprograms!''')
print('''Greetings,\
    programs!''')
print("""Greetings,
    Programs!""")

# spaces/indentations in Python is IMPORTANT!

# a simple hash in front of any designated code will comment it out
# conversely, highlighting a designated section then cmd + / will comment it out as well

# Literal Constants
# you use the value literally. It's a constant because its value cannot be changed.
5, 1.23, "This is a string", "It's a Str!"

# Numbers
# Integers and Floats indicated by the presence and lack of decimal point.
# TODO: Check if int type can be an integer of any size

# Int
2, 10, 100, 1001
# Float
2.12, 3.14, 4.20, 100.00, 52.3E-4

# Strings
# strings are immutable & sequence of characters within quotes
'This is in a single quote' | "This is in a double quote" | '''This is triple quotes'''
# triple quotes are NOT comments. It shows up grey bc dum, but will be evaluated.

# method format, basically matching.
varOne = "Yarp"
varTwo = "Narp"

print("{0} is {1} is {0}".format(varOne, varTwo))
print("{1} is {0} is {1}".format(varOne, varTwo))
print("{name} read the {book}".format(name='James', book='Bible'))

# Tuple~
language = ('Python', '3')
print("We are learning {0[0]} {0[1]}!".format(language))

# this doesn't work the way I thought it might, but maybe for dictionary?
# TODO: Check this out again with dictionary
complexLanguage = ('Python', '3.5'), ('Ruby', '3')
print("I'm learning {0[0]} {0[1]} right now, but waiting for {1[0]} {1[1]}!")

# Variables
# no need for var in front, just standard syntax rules
name = 'James'
numberOne = 1
floatingNumberOne = 1.0