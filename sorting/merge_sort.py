def merge_sort(numbers: list[float], low: int, high: int) -> list[float]:
    if (low >= high):
        return numbers
    mid = (low + high) // 2
    merge_sort(numbers, low, mid)
    merge_sort(numbers, mid + 1, high)
    merge(numbers, low, mid, mid + 1, high)
    return numbers

def merge(numbers: list[float], low_a: int, high_a: int, low_b: int, high_b: int) -> list[float]:
    tmp = numbers[:]
    
    i = low_a
    j = low_b
    k = low_a

    # Copying smallest elements until smaller list is exhausted
    while (i <= high_a and j <= high_b):
        if tmp[i] <= tmp[j]:
            # numbers[i + j] cannot be used as it will leave out holes in between that won't get filled, rather next elements will get filled which for this stack frame are out of context
            numbers[k] = tmp[i]
            i += 1
        else:
            numbers[k] = tmp[j]
            j += 1
        k += 1

    # Copying remaining elements
    if i > high_a:
        while(j <= high_b):
            numbers[k] = tmp[j]
            j += 1
            k += 1
    else:
        while(i <= high_a):
            numbers[k] = tmp[i]
            i += 1
            k += 1

    return numbers
