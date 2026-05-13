import sys
from binary_search import binary_search

# # Input by interrupts
# input_size = int(input("Enter size of the list: "))
# elements = []

# print(f"Enter the {input_size} elements of the list")
# for i in range(input_size):
#     element = float(input())
#     elements.append(element)

# print("Elements given by user are:\n", elements)

# Input from args
input_numbers: list[float] = []

for i in range(1, len(sys.argv)):
    input_numbers.append(float(sys.argv[i]))

print("Elements given by user are:\n", input_numbers)

search_element = float(input('Enter the element to be searched: '))

search_index = binary_search(search_element, input_numbers)

if search_index == -1:
    print(f"{search_element} was not found in the list")
else:
    print(f"{search_element} was found at position {search_index} in the list")
