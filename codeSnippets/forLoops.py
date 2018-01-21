# Python stops one number before the last.

for i in range(1, 20):
    print("i is now {}".format(i))

number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for i in range(0, len(number)):
    print(number[i])

# modified
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i], end='')
# the end='' removes next line condition.

# converting from str to int, cleaning it up, then back to str via interpolation.
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)

print("The number is {} ".format(newNumber))

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char
        # print(cleanedNumber)

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ["not pinin'", "no more", "a stiff", "bereft of life"]:
    print("This parrot is " + state)
    print("This parrot is {}".format(state))

for i in range(0, 100, 5):
    print("i is {}".format(i))

# Multiplication Table, demonstrated by nested loops
for i in range(1, 12):
    for j in range(1, 12):
        print("{1} times {0} is {2}".format(i, j, i * j))
    # print("===============")
    print('')