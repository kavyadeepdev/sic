from partition import partition_list

def quick_sort(numbers: list[float], low: int, high: int) -> list[float]:
    if low < high:
        pivot_index = partition_list(numbers, low, high)
        quick_sort(numbers, low, pivot_index - 1)
        quick_sort(numbers, pivot_index + 1, high)
    return numbers