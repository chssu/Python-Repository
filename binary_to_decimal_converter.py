#!/usr/bin/env python3

"""
Program which asks the user whether they want to convert from decimal to binary,
or binary to decimal. The program then prompts the user to enter either a decimal
integer or a binary string depending on their previous selection. The program then
converts the input to either binary or decimal, depending on the selection.
"""

def decimal_to_binary():
    decimal = int(input('Please enter a positive integer: '))
    arr = []
    while decimal > 0:
        arr.append(decimal % 2)
        decimal = int(decimal/2)
    binary_string = [str(x) for x in arr[::-1]]
    print(''.join(binary_string))


def binary_to_decimal():
    binary_list = list(input('Please enter a binary number (no spaces or commas): '))
    total = 0
    for x in binary_list:
        total = total * 2 + int(x)
    print(total)


print('''Please select an operation:
1) Decimal to binary
2) Binary to decimal\n''')

while True:
    operation_selection = input('[1/2]:')
    if operation_selection == '1':
        decimal_to_binary()
        break
    elif operation_selection == '2':
        binary_to_decimal()
        break
    else:
        print("Invalid selection. You must select either '1' or '2'. Try again...\n")
