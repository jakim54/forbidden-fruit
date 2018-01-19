# Python stops one number before the last.

# for i in range(1, 20):
#     print("i is now {}".format(i))

number = "9,223,372,036,854,775,807"
cleanedNumber = ''

# for i in range(0, len(number)):
#     print(number[i])

# modified
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         print(number[i], end='') #the end='' removes next line condition.

# converting from str to int, cleaning it up, then back to str via interpolation.
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)

print("The number is {} ".format(newNumber))

