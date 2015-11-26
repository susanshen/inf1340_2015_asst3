#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists. """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


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


def selection(t, f):
    """
    Perform select operation on table t that satisfy condition f.

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    ># Define function f that returns True iff
    > # the last element in the row is greater than 3.
    > def f(row): row[-1] > 3
    > select(R, f)
    [["A", "B", "C"], [4, 5, 6]]

    """

    return []


def projection(t, r):
    """
    Perform projection operation on table t
    using the attributes subset r.

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    > projection(R, ["A", "C"])
    [["A", "C"], [1, 3], [4, 6]]

    """

    return []


def cross_product(t1, t2):
    """
    Return the cross-product of tables t1 and t2.

    Example:
    > R1 = [["A", "B"], [1,2], [3,4]]
    > R2 = [["C", "D"], [5,6]]
    [["A", "B", "C", "D"], [1, 2, 5, 6], [3, 4, 5, 6]]


    """

    return []







#############



table_1 = [["Number", "Surname", "Ages"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

table_2 = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]


def schema_check(table1, table2):
    """
    This function takes two tables as input and ensures that they have the same schema, which in this
    case means that the title of each column is exactly the same and each table has the same number of columns
    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: None
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same schema

    """

    # compares the first row of each table to ensure the titles and number of columns match
    if table1[0] != table2[0]:
        raise MismatchedAttributesException


def union(table1, table2):
    """
    Combines input tables and returns a table that contains all unique rows that appear in either input tables

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: a table with all unique rows from either input tables
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same schema
    """

    schema_check(table1, table2)
    # combines the two input tables, then removes the duplicates from the combined table
    union_table = table1 + table2
    return remove_duplicates(union_table)




def intersection(table1, table2):
    """
    Combines input tables and returns a table that contains all unique rows that appear in both input tables

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: a table with all unique rows from both input tables
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same schema

    """

    schema_check(table1, table2)
    intersection_list = []
    # iterates through rows in table one and table two
    for lists1 in table1:
        for lists2 in table2:
            # compares rows between the two tables and appends matching rows to the empty list
            if lists1 == lists2:
                intersection_list.append(lists1)
    return intersection_list




def difference(table1, table2):
    """
    Combines input tables and returns a table that contains all unique rows that appear in
    the first input table but not the second as well as the title row.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: a table with all unique rows from the first input table and the title row
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same schema

    """

    schema_check(table1, table2)
    # pulls column titles from table one for input in the final table
    column_titles = table1[0]
    count = 0
    while count < len(table1):
        # iterates though rows in each table
        for lists1 in table1:
            for lists2 in table2:
                # compares rows and removes matching rows from table one
                if lists1 == lists2:
                    table1.remove(lists1)
        count += + 1
    # inserts column titles as top row and returns the final table
    table1.insert(0,column_titles)
    return table1


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


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """

    pass
