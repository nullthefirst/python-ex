def square_root(number):
    if number < 1:
        raise ValueError("Only positive whole numbers allowed")

    # Edge case - 1 is the square root of 1
    if number == 1:
        return number

    # Loop through all integers before the input number until the correct
    # integer that produces the number as a square is derived
    for num in range(number):
        if num * num == number:
            return num
