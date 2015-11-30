#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. Kanadia

Computer-based immigration office for Kanadia

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

import re
import datetime
import json

######################
## global constants ##
######################
REQUIRED_FIELDS = ["passport", "first_name", "last_name",
                   "birth_date", "home", "entry_reason", "from"]

######################
## global variables ##
######################
'''
countries:
dictionary mapping country codes (lowercase strings) to dictionaries
containing the following keys:
"code","name","visitor_visa_required",
"transit_visa_required","medical_advisory"
'''
COUNTRIES = None

with open("test_jsons/test_returning_citizen.json", "r") as entry_record_reader:
    entry_record_contents = entry_record_reader.read()
    test_return = json.loads(entry_record_contents)

with open("test_jsons/countries.json", "r") as countries_reader:
    countries_contents = countries_reader.read()
    countries = json.loads(countries_contents)


def entry_record_check(input_file):
    for dictionary in input_file:
        control_flag = "T"
        for key in dictionary:
            value1 = dictionary.get(key)
            if value1 == "":
                control_flag = "F"
            if key == REQUIRED_FIELDS[-1]:
                list2 = value1
                if (list2['city']) == "":
                    control_flag = "F"
                elif (list2['region']) == "":
                    control_flag = "F"
                elif (list2['country']) == "":
                    control_flag = "F"
            if key == REQUIRED_FIELDS[4]:
                list2 = value1
                if (list2['city']) == "":
                    control_flag = "F"
                elif (list2['region']) == "":
                    control_flag = "F"
                elif (list2['country']) == "":
                    control_flag = "F"
        if control_flag == "F":
            print(dictionary)


def location_check(input_file, countries_file):
    for dictionary in input_file:
        control_flag = "F"
        for key in dictionary:
            value1 = dictionary.get(key)
            if key == REQUIRED_FIELDS[-1]:
                list1 = value1
                pvalue1 = (list1['country'])
                for key2 in countries_file:
                    if key2 == pvalue1:
                        control_flag = "T"
        if control_flag == "F":
            print ["Reject"]
        else:
            print ["Accept"]


#def validate_visa(input_file, visa_code, x, date_string):


#####################
# HELPER FUNCTIONS ##
#####################


def is_more_than_x_years_ago(x, date_string):
    """
    Check if date is less than x years ago.

    :param x: int representing years
    :param date_string: a date string in format "YYYY-mm-dd"
    :return: True if date is less than x years ago; False otherwise.
    """

    now = datetime.datetime.now()
    x_years_ago = now.replace(year=now.year - x)
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')

    return (date - x_years_ago).total_seconds() < 0


def decide(input_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains
        cases to decide
    :param countries_file: The name of a JSON formatted file that contains
        country data, such as whether an entry or transit visa is required,
        and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are:
        "Accept", "Reject", and "Quarantine"
    """
    for dictionary in input_file:
        control_flag = "F"
        for key in dictionary:
            value1 = dictionary.get(key)
            if key == "home":
                list1 = value1
                pvalue1 = (list1['country'])
                if pvalue1 != "KAN":
                    for key2 in countries_file:
                        if key2 == pvalue1:
                            control_flag = "T"
                else:
                    control_flag = "T"
        if control_flag == "F":
            print ["Reject"]
        else:
            print ["Accept"]


def valid_passport_format(passport_number):
    """
    Checks whether a passport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """
    # TESTED & WORKING

    valid_passport_regex = re.compile(r'\w\w\w\w\w-\w\w\w\w\w-\w\w\w\w\w-\w\w\w\w\w-\w\w\w\w\w')
    valid_passport_match = valid_passport_regex.search(passport_number)
    if valid_passport_match is not None:
        return True
    else:
        return False


def valid_visa_format(visa_code):
    """
    Checks whether a visa code is two groups of five alphanumeric characters
    :param visa_code: alphanumeric string
    :return: Boolean; True if the format is valid, False otherwise

    """

    # TESTED & WORKING

    valid_visa_regex = re.compile(r'\w\w\w\w\w-\w\w\w\w\w')
    valid_visa_match = valid_visa_regex.search(visa_code)
    if valid_visa_match is not None:
        return True
    else:
        return False


def valid_date_format(date_string):
    """
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """

    # TESTED & WORKING

    valid_date_format_regex = re.compile(r'\d\d\d\d-\d\d-\d\d')
    valid_date_format_match = valid_date_format_regex.search(date_string)
    if valid_date_format_match is not None:
        return True
    else:
        return False


#def main():

# input_file =
# countries_file =



#main()
#entry_record_check(test_return)
#location_check(test_return, countries)
#decide(test_return, countries)
#valid_passport_format("JMZ0S-89IA9-OTCLY-MQILJ-P7CTY")
#valid_visa_format("2f2h2-2sdf2")
#valid_date_format("1997-89-00")