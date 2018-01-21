greeting = "Bruce"
_myName = "James"
Tim45 = "Good"
Tim_Was_30 = "Hello"
Greeting = "BRUCE"

print(Tim45 + Tim_Was_30 + 'shiueetttt')

age = 25
print(age)

# this will throw an error of type conflict
# print(greeting + age)

# Python will use float by default, and must specify integer
a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b) # This returns 4.0 as a float
print(a // b) # This returns 4, as an integer
print(a % b)

# loop example
for i in range(1, a // b):
    print("i equals", i)

# comma works within the print function:
# i equals 1
# i equals 2
# i equals 3

# This results in 12, PEMDAS appropriate
print((((a + b) // 3) -4) * 12)

# Type, top string
parrot = "Norwegian Blue"
print(parrot)

# will take the 3rd index of value parrot, which is w.
print(parrot[3])

# conversely, you can also count backwards, -1 being e
print(parrot[-1])

# range starting from index 0, upto 6, Norweg.
print(parrot[0:6])

# default 0 range if unspecified, Norweg
print(parrot[:6])

# number specified after colon is to the end, ian Blue
print(parrot[6:])

# third number specified will indicate the n times to skip upto the range specified within the first two numbers.
print(parrot[0:6:2])

# From index 1, which is a comma to the end as it's unspecified and print every 4th character which results in
# ,,,,,
numberRange = "9,223,372,036,854,775,807"
print(numberRange[1::4])

# same as before
# 123456789
numberRange2 = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numberRange2[0::3])

# to print strings only, you do not need to use +
print("yo" "this" "is")
# comma did not add spaces in this case, but for the loop example it did?
print("hm", "space via comma", "word")

# functions/methods like so
print("Hello " * 5)
# Python is sick!
print(("Hello" + " ") * (5 + 4))
print("Hello " * 5 + "4")

# comparison within print?
today = "friday"
print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in "fjord")