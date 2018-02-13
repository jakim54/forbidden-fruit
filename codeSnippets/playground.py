# Took this for loop to really understand for loops.
# more nested for loop examples

number = "9,223,372,036,854,775,807"

for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i])

    if number[i] == ',':
        print("comma")

for a in range(0, 3):
    for b in range(0, 5):
        print(a, b)
print("End of Line")

for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            print(i, j, k)
print("End of Line")

pyramidWidth = 10
# half pyramid
for i in range(0, pyramidWidth):
    for j in range(0, pyramidWidth - i):
        print(" ", end="")
    for k in range(0, i + 1):
        print("0", end="")
    print("")

# full  pyramid
for i in range(0, pyramidWidth):
    for j in range(0, pyramidWidth - i):
        print(" ", end="")
    for k in range(0, 2 * i + 1):
        print("0", end="")
    print("")

# while loop examples with continue/break:

# prints 0, 1, 2 before exiting loop
a = 0
while a < 5:
    print(a)
    if a == 2:
        break
    a += 1

# breaks when result is 0
for i in range(1, 20):
    print(i)
    if i % 7 == 0:
        break

# prints 3, 6, 9, 12, 15, 18
for i in range(1, 20):
    if i % 3:
        continue
    print(i)

# # prints everything but 12 and 18
for i in range(1, 20):
    if i % 2 == 0 and i % 3 == 0:
        continue
    print(i)