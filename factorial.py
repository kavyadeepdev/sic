def find_factorial(number: int) -> int:
    if number == 0 or number == 1:
        return 1
    return number * find_factorial(number - 1)