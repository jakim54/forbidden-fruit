# Create a program that takes an IP address entered at the keyboard and
# prints out the number of segments and the length of each segments.
# An IP address consists of 4 numbers, separated from each other with
# a full stop.Your program should only count however many were entered.

# Examples of the input you may get are:
#     127.0.0.1
#     .192.168.0.1
#     10.0.123456.255
#     172.16
#     255

# Your program should work even with an invalid IP address. We're just
# interested in the number of segments and how long each one is.

# Once you have a working program, test for these:
#     .123.45.678.91
#     123.4567.8.9.
#     123.156.289.10123456
#     10.10t.10.10
#     12.9.34.6.12.90
#     ''

# This challenge is to help you practice for loops & if/else statements.
# Although you can use other techniques, such as format/split etc, that's not
# the approach we're looking for here.

# My initial solution:
# Misunderstood the assignment, counting lines per segment and not overall.
addressIP = input("Insert IP address here: ")
lengthOfAddress = len(addressIP)
segmentCount = 0

if addressIP == '':
    print("Nothing was entered")
else:
    for char in addressIP:
        if char == ".":
            segmentCount += 1

    print("{0} is {1} count long and has {2} total segments.".format(addressIP, lengthOfAddress, segmentCount))
# TODO: separate the char count to each segment and refactor so that the if/else is tucked inside the for loop and not vice versa.

# Master solution:
ipAddress = input("Please enter an IP Address: ")
character = ""
segment = 1
segmentLength = 0

for character in ipAddress:
    if character == '.':
        print("Segment {0} contains {1} characters.".format(segment, segmentLength))
        segment += 1
        segmentLength = 0
    else:
        segmentLength += 1

if character != '.':
    print("Segment {0} contains {1} characters.".format(segment, segmentLength))