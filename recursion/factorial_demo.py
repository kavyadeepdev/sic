import sys
from factorial import find_factorial

input_number = int(sys.argv[1])

factorial_number = find_factorial(input_number)

print(f"Factorial of {input_number} is {factorial_number}")