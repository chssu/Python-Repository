#!/usr/bin/env python3

"""
This program takes an input, N, from the user in the form of an integer.
The program then prints the fibonacci sequence to the Nth term 
(with 0 being the first term).
"""

from math import sqrt

n = int(input('Please enter a number: '))
sequence_list = []
term = 0

for x in range(n):
    term = (((1 + sqrt(5))/2)**x - ((1 - sqrt(5))/2)**x)/sqrt(5)
    sequence_list.append(int(term))

sequence_list_string = [str(x) for x in sequence_list]
print('The fibonacci sequence to the ' + str(n) + 'th place (including 0) is:')
print(", " . join(sequence_list_string))
