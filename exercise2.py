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


def checksum (upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a strong
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    # check type of input
    # raise TypeError if not string

    # check length of string
    # raise ValueError if not 12

    # convert string to array
    # hint: use the list function

    # generate checksum using the first 11 digits provided
    # check against the the twelfth digit

    # return True if they are equal, False otherwise

    if isinstance(upc, str):
        if len(upc) == 12:
            upc = upc.split(',')
            oddsum = upc[0, 2, 4, 6, 8, 10, 12]
            oddsum_times_3 = oddsum * 3
            evensum = upc[1, 3, 5, 7, 9]
            totalsum = oddsum_times_3 + evensum
            checksum = totalsum % 10
            if checksum != 0:
                True
            else:
                checksum = 10 - checksum
        else:
            raise ValueError("Invalid length")
    else:
        raise TypeError

    else:
    return False

