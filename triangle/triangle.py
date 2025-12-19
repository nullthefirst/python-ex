def is_valid_lengths(sides):
    a, b, c = sides

    if a <= 0 or b <= 0 or c <= 0:
        return False
    else:
        return True

def is_differing_sides(sides):
    a, b, c = sides

    if a + b >= c and b + c >= a and a + c >= b:
        return True
    else:
        return False


def equilateral(sides):
    a, b, c = sides

    if is_valid_lengths(sides):
        if a == b and b == c and a == c:
            return True
        else:
            return False
    else:
        return False


def isosceles(sides):
    a, b, c = sides

    if is_valid_lengths(sides) and is_differing_sides(sides):
        if a == b or b == c or a == c:
            return True
        else:
            return False
    else:
        return False


def scalene(sides):
    a, b, c = sides

    if is_valid_lengths(sides) and is_differing_sides(sides):
        if a != b and b != c and a != c:
            return True
        else:
            return False
    else:
        return False
