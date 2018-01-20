# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments and the length of each segments.

# An IP address consists of 4 numbers, separated from each otehr with a full stop. 
# Your program should just count however many are entered.

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

# This challenge is intended to help you practice for-loops and if/else statements.
# So, although you can use other techniques, such as format/split etc, that's not
# the approach we're looking for here.

# TODO:

# receivedData = '127.0.0.1', '.192.168.0.1', '10.0.123456.255', '172.16', '255'
# testData = '.123.45.678.91', '123.4567.8.9', '123.156.289.10123456', '10.10t.10.10', '12.9.34.6.12.90', ''