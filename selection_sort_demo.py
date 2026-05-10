from selection_sort import selection_sort
import sys

input_elements = []
for i in range(1, len(sys.argv)):
    input_elements.append(float(sys.argv[i]))

print("User entered list:\n", input_elements)

selection_sort(input_elements)

print("Sorted list:\n", input_elements)