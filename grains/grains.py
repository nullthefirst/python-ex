def calculator():
    board = dict()

    for i in range(1, 65):
        board[i] = 1

    for key, value in board.items():
        if key > 1:
            board[key] = board[key - 1] * 2

    return board


def square(number):
    if number < 1 or number > 64:
        # when the square value is not in the acceptable range
        raise ValueError("square must be between 1 and 64")

    return calculator()[number]


def total():
    reward = 0

    for key, value in calculator().items():
        reward += value

    return reward

