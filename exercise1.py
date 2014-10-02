#!/usr/bin/env python3


""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    letter_grade = ""
    gpa = 0.0

    #list of top number in grade range
    # & list of letter grade

    if type(grade) is str:
        print ("letter") # remove this line once the code is implemented
        # check that the grade is one of the accepted values
        letter_grade_dictionary = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "FZ": 0.0}
        if grade in letter_grade_dictionary:
            gpa = letter_grade_dictionary[grade]
        else:
            raise TypeError ("Invalid letter grade passed as a parameter.") # assign grade to letter_grade
    elif type(grade) is int:
        print("mark") # remove this line once the code is implemented
        if 0 <= grade <= 100: # check that grade is in the accepted range
            # need to do a forloop - started with (for i in xxxx )# for loops and a break if the number is found
        # convert the numeric grade to a letter grade
        # assign the value to letter_grade
        # hint: letter_grade = mark_to_letter(grade)
        else:
            raise TypeError ("Invalid percentage grade passes as a parameter.")
    else:
        # raise a TypeError exception
        raise TypeError("Invalid type passed as parameter")

    # write a long if-statement to convert letter_grade
    # assign the value to gpa
    if letter_grade == "A":
        gpa = 4.0

    return gpa

