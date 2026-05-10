from partition import partition
n = int(input("Enter number of oranges: "))
oranges = [float(orange) for orange in input(f"Enter diameter of oranges (1 - {n}): ").split()]

partition(oranges)

print(oranges)
