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
        print('UPC is a string')
    else:
        raise TypeError

    if len(upc) = 12
        print('UPC is 12 characters')
    else:
        raise ValueError

    oddsum = (upc[0] + upc[2] + upc[4] + upc[6] + upc[8] + upc[10] + upc[12])
    evensum = (upc[1] + upc[3] + upc[5] + upc[7] + upc[9] + upc[11])

    if len(upc) != 12 raise ValueError("Invalid length")
    else:
        (((oddsum * 3) + evensum) % 10)




    return False

