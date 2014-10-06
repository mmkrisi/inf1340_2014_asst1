#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def checksum(upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under)
    """
    if type(upc) is not str:
        raise TypeError("Invalid type")

    # if we get this far, we know that upc is a string
    if len(upc) != 12:
        error_length = len(upc) - 12
        if error_length < 0:
            error_length = abs(error_length)
            # show how many digits under 12 are inputted
            raise ValueError("Invalid length of UPC number: short by", error_length, "digits")
        else:
            # show how many digits over 12 are inputted
            raise ValueError("Invalid length of UPC number: over by", error_length, "digits")

    # if we get this far, we know that upc is a string of length 12
    # Now we can start computing

    # turn string into a list of chars
    input_list = list(upc)
    for(index, char) in enumerate(input_list):
        input_list[index] = int(char)
    odd_sum = sum(input_list[0::2])
    odd_sum_triple = odd_sum * 3
    even_sum = sum(input_list[1:11:2])
    total_sum = odd_sum_triple + even_sum
    # generate checksum using the first 11 digits provided
    check_sum_modulo = total_sum % 10
    # check against the twelfth digit
    # return True if they are equal, False otherwise
    if check_sum_modulo == 0:
        return True
    elif check_sum_modulo !=0:
        check_sum_modulo = 10 - check_sum_modulo
        if check_sum_modulo == input_list[11]:
            return True
        else:
            return False
