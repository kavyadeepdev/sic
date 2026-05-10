def partition(numbers: list[float]) -> list[float]:
    pivot = numbers[-1]
    j = 0
    for i in range(len(numbers)):
        if numbers[i] < pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j += 1
    numbers[-1], numbers[j] = numbers[j], numbers[-1]
    return numbers
