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
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    # check type of input
    # raise TypeError if not string

    # check length of string
    # raise ValueError if not 12

    # convert string to array
    # hint: use the list function

    # generate checksum using the first 11 digits provided
    # check against the twelfth digit

    # return True if they are equal, False otherwise

    if type(upc) is str:
        if len(upc) == 12:

            list(upc) # turn string into a list of chars #list(string)
            for char in (upc):
                char = int[upc] # turn your list of chars into a list of ints # int('1')

            # upc = upc.split(',')

            # sum a slice of the list
            odd_sum = upc[0] + upc[2] + upc4, 6, 8, 10, 12]
            odd_sum_times_3 = odd_sum * 3
            even_sum = upc[1, 3, 5, 7, 9]
            total_sum = odd_sum_times_3 + even_sum
            check_sum_modulo = total_sum % 10
            if check_sum_modulo != 0:
                True
            else:
                check_sum_modulo = 10 - check_sum_modulo
        else:
            error_length = len(upc) - 12
            if error_length < 0:
                    error_length = abs(error_length)
                    raise ValueError("Invalid length of UPC number: short by", error_length, "numbers") # showing how many digits under are input
            else:
                    raise ValueError("Invalid length of UPC number: over by", error_length, "numbers") #we need to add how many digits over 12 are input
    else:
        raise TypeError("Invalid type")
    return True


   

