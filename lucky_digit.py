# Program to find lucky number
import pdb

pdb.set_trace()

input_number = int(input("Enter a number to find your lucky digit: "))

while input_number // 10 != 0:
    digit_sum = 0
    while input_number != 0:
        digit_sum += input_number % 10
        input_number //= 10
    input_number = digit_sum

print(f"Your lucky digit is {input_number}")
