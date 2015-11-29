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
#   print test_return

with open("test_jsons/countries.json", "r") as countries_reader:
    countries_contents = countries_reader.read()
    countries = json.loads(countries_contents)


def entry_record_check():
    for dictionary in test_return:
        control_flag = "T"
#        print "Start"
        for key in dictionary:
            value1 = dictionary.get(key)
            if key == "from":
                #print("1-key", key)
                #print("2-value1", value1)
                for key1 in value1:
                    value2 = dictionary.get(key1)
                    pvalue0 = value1.values()
                    if pvalue0[0] == "":
                        control_flag = "F"
                    elif pvalue0[1] == "":
                        control_flag = "F"
                    elif pvalue0[2] == "":
                        control_flag = "F"
            if key == "home":
                #print("1-key", key)
                #print("2-value1", value1)
                for key1 in value1:
                    value2 = dictionary.get(key1)
                    pvalue0 = value1.values()
                    if pvalue0[0] == "":
                        control_flag = "F"
                    elif pvalue0[1] == "":
                        control_flag = "F"
                    elif pvalue0[2] == "":
                        control_flag = "F"
                    #print("3-key1", key1)
                    #print("4-value2", value2)
                    #print("4a-pvalue0", pvalue0[0])
        if control_flag == "F":
            print(dictionary)


#            if (dictionary.get(key)) == "":
#                control_flag = "F"
#            if key == "from":
#                print("2-", key)
#                for key1, value1 in key.iteritems(key1):
#                    print key1, value1
                    #print(dictionary.get(key))
                 #   if key1 == "city":
                    #    print("3")
         #               control_flag = "F"
         #   if control_flag == "F":
              #  print(dictionary)


def location_check():
    for dictionary in test_return:
        control_flag = "T"
        for key in dictionary:
            if (dictionary.get(key)) == "":
                control_flag = "F"
        if control_flag == "F":
            print(dictionary)
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

    return ["Reject"]


def valid_passport_format(passport_number):
    """
    Checks whether a passport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """
    valid_passport_regex = re.compile(r'\d\d\d\d\d-\d\d\d\d\d-\d\d\d\d\d-\d\d\d\d\d-\d\d\d\d\d')
    valid_passport_match = valid_passport_regex.search(entry_record_contents)
    if valid_passport_match is None:
        return False
    else:
        return True


def valid_visa_format(visa_code):
    """
    Checks whether a visa code is two groups of five alphanumeric characters
    :param visa_code: alphanumeric string
    :return: Boolean; True if the format is valid, False otherwise

    """


def valid_date_format(date_string):
    """
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """

    return False


entry_record_check()

#valid_passport_format("JMZ0S-89IA9-OTCLY-MQILJ-P7CTY")