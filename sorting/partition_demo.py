import sys
from partition import partition_list

numbers = [float(num) for num in sys.argv[1:]]

print("Numbers before partition:\n", numbers)

partition_list(numbers, 0, len(numbers) - 1)

print("Numbers after partition:\n", numbers)