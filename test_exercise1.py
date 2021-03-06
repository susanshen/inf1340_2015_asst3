#!/usr/bin/env python

""" Assignment 3, Exercise 1, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Deanna Wong, Alyha Shahrukh & Shu Yun Susan Shen'
__email__ = "deanna.wong@mail.utoronto.ca, alyha.shahrukh@mail.utoronto.ca & shuyun.shen@mail.utoronto.ca"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise1 import selection, projection, cross_product, UnknownAttributeException


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

R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]

R_empty = []

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
    Check if employee represented by row is AT LEAST 30 years old and makes MORE THAN 3500.
    :param row: A List in the format:
        [{Surname}, {FirstName}, {Age}, {Salary}]
    :return: True if the row satisfies the condition.
    """
    return row[-2] >= 30 and row[-1] > 3500


def filter_r(row):
    """
    The last element in the row is greater than 3 for table R.
    :param row: A List in the format:
        [{A}, {B}, {C}]
    :return: True if the row satisfies the condition.
    """
    return row[-1] > 3


def wrong_filter_employees(row):
    """
    Conditions do not satisfy parameter on list.
    return: False
    """
    return row[-2] <= 20

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


def test_selection2():
    result = [["A", "B", "C"], [4, 5, 6]]

    assert is_equal (result, selection(R, filter_r))


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


def test_projection2():
    result = [["Age"],
              [25],
              [40],
              [36],
              [40]]

    assert is_equal(result, projection(EMPLOYEES, ["Age"]))


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


# Error test cases

def selection_error():
    """
    Test if wrong parameters for list.
    """
    assert wrong_filter_employees() == True


def projection_error():
    """
    Tests attributes not found on list.
    """
    assert projection(EMPLOYEES,["Hello"]) == False


def cross_product_error():
    """
    Tests when a list is empty.
    """
    assert cross_product(R1,R_empty) == True




