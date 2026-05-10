from partition import partition
n: int = int(input("Enter number of oranges: "))
oranges = input(f"Enter diameter of oranges (1 - {n}): ").split()

partition(oranges)

print(oranges)
