#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists. """

__author__ = 'Deanna Wong, Alyha Shahrukh & Susan Shen'
__email__ = "deanna.wong@mail.utoronto.ca, alyha.shahrukh@mail.utoronto.ca & shuyun.shen@mail.utoronto.ca"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


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

def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result

class UnknownAttributeException(Exception):
    """
    Raised when attempting set operations on a table
    that does not contain the named attribute
    """
    pass

def filter_employees(row):
    return row[-2] >= 30 and row[-1] > 3500

######################

def selection(t, f):
    """
    Perform select operation on table t that satisfy condition f.

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    ># Define function f that returns True if
    > # the last element in the row is greater than 3.
    > def f(row): row[-1] > 3
    > select(R, f)
    [["A", "B", "C"], [4, 5, 6]]

    """

    selection_table = []

    for row in t:
    #check if row on table satisfies function and add to created table
        if f(row) is True:
            selection_table.append(row)
        else:
            continue

    return selection_table

#selection (EMPLOYEES, filter_employees)

def projection(t, r):
    """
    Perform projection operation on table t
    using the attributes subset r.

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    > projection(R, ["A", "C"])
    [["A", "C"], [1, 3], [4, 6]]

    """

    projection_table = []
    location = []
    for item in range(len(r)):
        search = r[item]
        for i in range(len(t[0])):
            title = t[0][i]
            if search == title:
                location.append(i)
    if len(location) == 0:
        raise UnknownAttributeException

    for i in range(len(t)):
        individual_lines = []
        line = t[i]
        for j in range(len(location)):
            index_loc = location[j]
            info_to_pull = line[index_loc]
            individual_lines.append(info_to_pull)
        projection_table.append(individual_lines)

    return projection_table

#projection (EMPLOYEES, ["Surname","FirstName"])


def cross_product(t1, t2):
    """
    Return the cross-product of tables t1 and t2.

    Example:
    > R1 = [["A", "B"], [1,2], [3,4]]
    > R2 = [["C", "D"], [5,6]]
    [["A", "B", "C", "D"], [1, 2, 5, 6], [3, 4, 5, 6]]

    """
    #combine table headings
    column_titles = t1[0] + t2[0]
    cross_table = []

    #remove headings from tables
    del t1[0]
    del t2[0]

    for list1 in t1:
        for list2 in t2:
            if list2 not in list1:
            #combines tables into new table (without headings)
                combined_table = list1 + list2
                cross_table.append(combined_table)
            else:
                continue
    #inserts heading back to new table
    cross_table.insert(0,column_titles)

    return cross_table

#cross_product(R1,R2)

