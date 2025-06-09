def steps(number):
    steps = 0

    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    elif number == 1:
        return steps
    else:
        state = number

        while state > 1:
            if state % 2 == 0:
                state = state / 2
                steps += 1
            else:
                state = (state * 3) + 1
                steps += 1

        return steps


output = steps(16)
print(output)
