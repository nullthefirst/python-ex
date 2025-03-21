"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40

PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes, taking in the number of layers.

    Args:
        number_of_layers (int): number of layers to be used in preparation.

    Returns:
        int: Total time in minutes multiplied by the 'PREPARATION_TIME' constant.
    """

    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculates the total elapsed number of minutes since preparation began.

    Args:
        number_of_layers (int): number of layers to be used in preparation.
        elapsed_bake_time (int): total time in minutes that baking has occured for.

    Returns:
        int: Total preparation time in minutes summed with the total baking time.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
