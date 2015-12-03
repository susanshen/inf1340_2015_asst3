#!/usr/bin/env python

""" Assignment 3, Exercise 1, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise1 import selection, projection, cross_product


###########
# TABLES ##
###########

EMPLOYEES = [["Surname", "FirstName", "Age", "Salary"],
             ["Smith", "Mary", 25, 2000],
             ["Black", "Lucy", 40, 3000],
             ["Verdi", "Nico", 36, 4500],
             ["Smith", "Mark", 40, 3900]]

R1 = [["Employee", "Department"],
      ["Smith", "sales"],
      ["Black", "production"],
      ["White", "production"]]

R2 = [["Department", "Head"],
      ["production", "Mori"],
      ["sales", "Brown"]]


#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):

    t1.sort()
    t2.sort()

    return t1 == t2


#####################
# FILTER FUNCTIONS ##
#####################
def filter_employees(row):
    """
    Check if employee represented by row
    is AT LEAST 30 years old and makes
    MORE THAN 3500.
    :param row: A List in the format:
        [{Surname}, {FirstName}, {Age}, {Salary}]
    :return: True if the row satisfies the condition.
    """
    return row[-2] >= 30 and row[-1] > 3500


###################
# TEST FUNCTIONS ##
###################

def test_selection():
    """
    Test select operation.
    """

    result = [["Surname", "FirstName", "Age", "Salary"],
              ["Verdi", "Nico", 36, 4500],
              ["Smith", "Mark", 40, 3900]]

    assert is_equal(result, selection(EMPLOYEES, filter_employees))


def test_projection():
    """
    Test projection operation.
    """

    result = [["Surname", "FirstName"],
              ["Smith", "Mary"],
              ["Black", "Lucy"],
              ["Verdi", "Nico"],
              ["Smith", "Mark"]]

    assert is_equal(result, projection(EMPLOYEES, ["Surname", "FirstName"]))


def test_cross_product():
    """
    Test cross product operation.
    """

    result = [["Employee", "Department", "Department", "Head"],
              ["Smith", "sales", "production", "Mori"],
              ["Smith", "sales", "sales", "Brown"],
              ["Black", "production", "production", "Mori"],
              ["Black", "production", "sales", "Brown"],
              ["White", "production", "production", "Mori"],
              ["White", "production", "sales", "Brown"]]

    assert is_equal(result, cross_product(R1, R2))






#TEST CASES FOR EXERCISE 3 OF ASSIGNMENT 2


from exercise3 import union, intersection, difference, schema_check, MismatchedAttributesException


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

# This table has a mismatched heading
GRADUATES_WRONG = [["Number", "Surname", "DOB"],
             [7274, "Robinson", "01/03/93"],
             [7432, "O'Malley", "10/10/01"],
             [9824, "Darkes", "09/08/76"]]

# This table has an extra column
MANAGERS_WRONG = [["Number", "Surname", "Age", "Sex"],
            [9297, "O'Malley", 56, "F"],
            [7432, "O'Malley", 39, "M"],
            [9824, "Darkes", 38, "M"]]


#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
    return set(map(tuple, t1)) == set(map(tuple, t2))


###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))


def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))


def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))

# Added student test begin here

def test_schema_titles():
    """
    Tests to make sure an error is thrown if the schema titles to not match
    """
    try:
        schema_check(GRADUATES_WRONG, MANAGERS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

    try:
        union(GRADUATES_WRONG, MANAGERS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

    try:
        intersection(GRADUATES_WRONG, MANAGERS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

    try:
        difference(GRADUATES_WRONG, MANAGERS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

def test_schema_columns():
    """
    Test to make sure an error is thrown if the amount of columns of the table do not match
    """
    try:
        schema_check(GRADUATES, MANAGERS_WRONG)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

    try:
        union(GRADUATES_WRONG, MANAGERS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

    try:
        intersection(GRADUATES_WRONG, MANAGERS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

    try:
        difference(GRADUATES_WRONG, MANAGERS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

def test_schema_error():
    """
    Tests that an error will not be thrown when schemas are matching
    """
    try:
        schema_check(GRADUATES, MANAGERS)
    except MismatchedAttributesException:
        assert False
    else:
        assert True



