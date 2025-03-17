def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    trace = 0

    while number > 1:
        if number % 2 == 0:
            number /= 2
            trace += 1
        else:
            number *=3
            number += 1
            trace += 1

    return trace
    # steps(number)
