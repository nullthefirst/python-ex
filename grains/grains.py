def bounty():
    positions = [n for n in range(1, 65)]
    board = {1: 1}

    for i in range(2, 65):
        value = board[i - 1] * 2
        board[i] = value

    return board

def square(number):
    if number <=0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:

        return bounty()[number]

def total():
    return sum(bounty().values())

print(total())
