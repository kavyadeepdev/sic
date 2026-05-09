def sequential_search(search_element, elements):
    for i in range(len(elements)):
        if elements[i] == search_element:
            return i
    return -1


input_size = int(input("Enter size of the list: "))
elements = []

print(f"Enter the {input_size} elements of the list")
for i in range(input_size):
    element = float(input())
    elements.append(element)

print("Elements given by user are:\n", elements)

search_element = float(input("Enter the element to be searched: "))

search_index = sequential_search(search_element, elements)

if search_index == -1:
    print(f"{search_element} was not found in the list")
else:
    print(f"{search_element} was found at position {search_index} in the list")
