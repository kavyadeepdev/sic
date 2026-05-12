import sys
from quick_sort import quick_sort

numbers = [float(num) for num in sys.argv[1:]]

print("Numbers before sorting:\n", numbers)

quick_sort(numbers, 0, len(numbers) - 1)

print("Numbers after sorting:\n", numbers)