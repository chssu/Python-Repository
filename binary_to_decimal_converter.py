def decimal_to_binary():
    print('decimal_to_binary')

def binary_to_decimal():
     print('binary_to_decimal')

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
