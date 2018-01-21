age = 20
name = "Bob"

print("{} was {} years old when he wrote this book".format(name, age))
print("Why is {} playing with that python?".format(name))
'''
format() lets substitutue each argument value in place of the specification
'''

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))

# fill with underscore (_) with text centered
# (^) to 11 width '___hello___'
print('{0:*^11}'.format('hello'))

# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

'''
Print ads a new line after eahc output. We can alter this with end=
'''
print('y', end='')
print('o', end='......')


# Escape characters using \
print('What\'s your name?')

print('This is the first line\nThis si the second line\t this is a tab')
# A single backlash indicate contune sentence in next line, not add line
print('THis is a sentence. \ This continue sin next line')

'''Raw strings
Always used in Regex. 
If you need to specify some strings where no special processing such as escape sequences are handled, then what you need is to specify a raw string b prefixing r or R to the string
'''
print(r'NewLines are indicated by \n')

# Acceptable varibables/ identifiers
_underscore = '_'
Capitalized_words = "C"
lowerCase_words = "l"
orWordsWithNumbers1 = "ore0"

# Use ; as a means to separate pieces of code to be run in a same line
i = 5 ; print(i)

'''
FLOW CONTROL
'''
number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    print('Congratz, you guessed it')
elif guess < number:
    print('No, it\'s a little higher than that')
else:
    print('No, it is a little lower than that')

print('Done!')

running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congratulations, you guessed it.')
        # this causes the while loop to stop
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
    # Do anything else you want to do here
print('Done!')

for i in range(1,5):
    print(i)
else:
    print('The loop is over')




