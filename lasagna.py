"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40


def bake_time_remaining(actual_min):
    """Calculate the bake time remaining.

    :param actual_min: int - actual time spent in oven
    
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remain_min = EXPECTED_BAKE_TIME - actual_min
    return remain_min



def preparation_time_in_minutes(number_of_layers):
    """Calculate the time taken for number of layers.

    :param number_of_layers: int - time spent in making layers
    
    Function that takes number of layers as an argument 
    and returns how musch time spent in making each layer.
    """
    min_spent = number_of_layers * 2
    return min_spent



def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    total_min = (number_of_layers*2)+elapsed_bake_time
    return total_min


# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
