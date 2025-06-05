def istriangle(sides):
    a, b, c = sides

    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif (a + b < c) or (b + c < a) or (c + a < b):
        return False
    else:
        return True


def equilateral(sides):
    a, b, c = sides

    if istriangle(sides):
        if a == b and b == c and a == c:
            return True
        else:
            return False
    else:
        return False


def isosceles(sides):
    a, b, c = sides

    if istriangle(sides):
        if equilateral(sides):
            return True
        else:
            if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
                return True
            else:
                return False
    else:
        return False


def scalene(sides):
    a, b, c = sides

    if istriangle(sides):
        if a != b and b != c and c != a:
            return True
        else:
            return False
    else:
        return False
