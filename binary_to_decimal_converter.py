#!/usr/bin/env python3

def decimal_to_binary():
    decimal = int(input('Please enter a positive integer: '))
    arr = []
    while decimal > 0:
        arr.append(decimal % 2)
        decimal = int(decimal/2)
    binary_string = [str(x) for x in arr[::-1]]
    print(''.join(binary_string))

def binary_to_decimal():
    print('binary_to_decimal')
    binary = int(input('Please enter a binary number (no spaces or commas): '))
    arr = [int(x) for x in binary]
    for x in binary:
        total = binary[x] * 2 + binary[x]

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
