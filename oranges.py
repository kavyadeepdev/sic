from sorting.partition import partition_list
n = int(input("Enter number of oranges: "))
oranges = [float(orange) for orange in input(f"Enter diameter of oranges (1 - {n}): ").split()]

partition_list(oranges, 0, len(oranges) - 1)

print(oranges)
