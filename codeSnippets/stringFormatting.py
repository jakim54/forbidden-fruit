age = 24

# str method to convert variable age from int
# single target
print("My age is " + str(age) + " years")

# method format replaces matching index items
print("My age is {0} years.".format(age))
# better example
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}.".format(31, "January", "March", "May", "July", "August", "October", "December"))

# using triple quote to format nicely
print("""January: {2}
    February: {0}
    March: {2}
    April{1}
    May: {2}
    June: {1}
    July: {2}
    August: {2}
    September: {1}
    October: {2}
    November: {1}
    December: {2}""".format(28, 30, 31))

# String Formatting Operator deprecated now for Python 3?
# Similar to Obj-C's.
print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

print("")

# Taste of for loop within the print statement
for i in range(1, 12):
    print("No. #2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))