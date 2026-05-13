import sys
from merge_sort import merge_sort

input_numbers = [float(number) for number in sys.argv[1:]]

print("Numbers before sorting:\n", input_numbers)

merge_sort(input_numbers, 0, len(input_numbers) - 1)

print("Numbers after sorting:\n", input_numbers)
