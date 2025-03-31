def factors(number):
    """ Factors are numbers that can be multiplied by themselves repeated to derive a number.

    :param number: int - number to derive factors from
    :return: list - the appropriate factors of the number supplied omitting the number itself
    """






def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    feedback = {
        "equals": "perfect",
        "less": "abundant",
        "more": "deficient"
    }

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")


