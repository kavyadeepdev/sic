import sys
from insertion_sort import insertion_sort

input_numbers = []

for i in range(1, len(sys.argv)):
    input_numbers.append(float(sys.argv[i]))

print("Elements given by user are:\n", input_numbers)

insertion_sort(input_numbers)

print("Sorted elements are:\n", input_numbers)
