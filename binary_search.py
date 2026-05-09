def binary_search(search_element, elements):
    low = 0
    high = len(elements) - 1
    while low <= high:
        mid = (low + high) // 2
        if elements[mid] == search_element:
            return mid
        elif elements[mid] > search_element:
            high = mid - 1
        else:
            low = mid + 1
    return -1
