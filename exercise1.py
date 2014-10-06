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
    # dictionary with letter grades and gpa to use for assigning grade to letter_grade
    letter_grade_gpa_dictionary = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "FZ": 0.0}
    # list of letter grades to use when input is an int
    list_of_letter_grade = ["A+", "A", "A-", "B+", "B", "B-", "FZ"]

    if type(grade) is str:
        #check that the grade is one of the accepted values
        if grade in letter_grade_gpa_dictionary.keys():
            #assign grade to letter_grade
            return letter_grade_gpa_dictionary.get(grade)
        else:
            raise ValueError("Invalid letter grade passed as a parameter.")

    elif type(grade) is int:
        # check that grade is in the accepted range
        if 0 <= grade <= 100:
            # write a long if-statement to convert numeric grade to letter_grade
            if 90 <= grade <= 100:
                grade = list_of_letter_grade[0]
            elif 85 <= grade < 90:
                grade = list_of_letter_grade[1]
            elif 80 <= grade < 85:
                grade = list_of_letter_grade[2]
            elif 77 <= grade < 80:
                grade = list_of_letter_grade[3]
            elif 73 <= grade < 77:
                grade = list_of_letter_grade[4]
            elif 70 <= grade < 73:
                grade = list_of_letter_grade[5]
            elif 0 <= grade < 70:
                grade = list_of_letter_grade[6]
             # assign grade to letter_grade
            return letter_grade_gpa_dictionary.get(grade)
        else:
            raise ValueError ("Invalid percentage grade passed as a parameter.")
    else:
       raise TypeError("Invalid type passed as parameter")


    if letter_grade in letter_grade_gpa_dictionary:
        # assign the value to gpa
        gpa = letter_grade_gpa_dictionary[grade]

    return gpa

