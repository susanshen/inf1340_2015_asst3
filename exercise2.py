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
from collections import Counter, defaultdict

##with open("test_jsons/test_returning_citizen.json", "r") as entry_record_reader:
##with open("C:\\Users\\wonke\\Desktop\\Python\\Deanna\\Assignment\\test_returning_citizen.json", "r") as entry_record_reader:
##    with open(input_file, "r") as entry_record_reader:
##        entry_record_contents = entry_record_reader.read()
##        test_return = json.loads(entry_record_contents)

##with open("test_jsons/countries.json", "r") as countries_reader:
##with open("C:\\Users\\wonke\\Desktop\\Python\\Deanna\\Assignment\\countries.json", "r") as countries_reader:
##    with open(countries_file, "r") as countries_reader:
##        countries_contents = countries_reader.read()
##        COUNTRIES = json.loads(countries_contents)

######################
## global constants ##
######################
REQUIRED_FIELDS = ["passport", "first_name", "last_name",
                   "birth_date", "home", "entry_reason", "from"]
#for question 1, need to check if all fields are present as well (iterate through this list)

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

    global x_years_flag
    x_years_flag = (date - x_years_ago).total_seconds() < 0


def valid_visa_format(visa_code):
    """
    Checks whether a visa code is two groups of five alphanumeric characters
    :param visa_code: alphanumeric string
    :return: Boolean; True if the format is valid, False otherwise

    """
    global valid_visa_format_flag
    valid_visa_regex = re.compile(r'\w\w\w\w\w-\w\w\w\w\w')
    valid_visa_match = valid_visa_regex.search(visa_code)
    if valid_visa_match is not None:
        valid_visa_format_flag = True
    else:
        valid_visa_format_flag = False


def valid_date_format(date_string):
    """
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """

    global valid_date_format_flag
    valid_date_format_regex = re.compile(r'\d\d\d\d-\d\d-\d\d')
    valid_date_format_match = valid_date_format_regex.search(date_string)
    if valid_date_format_match is not None:
        valid_date_format_flag = True
    else:
        valid_date_format_flag = False


def valid_passport_format(passport_number):
    """
    Checks whether a passport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """

    global valid_passport_format_flag
    valid_passport_regex = re.compile(r'\w\w\w\w\w-\w\w\w\w\w-\w\w\w\w\w-\w\w\w\w\w-\w\w\w\w\w')
    valid_passport_match = valid_passport_regex.search(passport_number)
    if valid_passport_match is not None:
        valid_passport_format_flag = True
    else:
        valid_passport_format_flag = False


def location_check(input_data, countries_file):
    global location_check_flag
    count = 0
    for key in countries_file:
        if input_data.upper() == key:
            count += 1
    if count == 0:
        location_check_flag = 'R'
    else:
        location_check_flag = 'A'


def visit_visa_check(input_data, countries_file):
    global visit_visa_check_flag
    for key in countries_file:
        if key.lower() == input_data.lower():
            if int(countries_file[key]['visitor_visa_required']) == 1:
                visit_visa_check_flag = True
            else:
                visit_visa_check_flag = False


def medical_advisory_check(input_data, countries_file):
    global medical_advisory_check_flag
    medical_advisory_check_flag = 'A'
    for key in countries_file:
        if key.lower() == input_data.lower():
            if countries_file[key]['medical_advisory'] == "":
                medical_advisory_check_flag = 'A'
            else:
                medical_advisory_check_flag = 'Q'


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

    with open(input_file, "r") as entry_record_reader:
        entry_record_contents = entry_record_reader.read()
        test_return = json.loads(entry_record_contents)

    with open(countries_file, "r") as countries_reader:
        countries_contents = countries_reader.read()
        COUNTRIES = json.loads(countries_contents)

        list = []
        i = 0
        while i < len(test_return):
            cnt_flag = 'F'
            
        # initializing all control flags to 'Accept' first
            for rf_key in REQUIRED_FIELDS:
                for key1 in test_return:
                    if rf_key not in key1:
                        cnt_flag = 'R'
            birth_date = (test_return[i]['birth_date'])
            passport = (test_return[i]['passport'])
            last_name = (test_return[i]['last_name'])
            first_name = (test_return[i]['first_name'])
            entry_reason = (test_return[i]['entry_reason'])
            from_country = (test_return[i]['from']['country'])
            from_region = (test_return[i]['from']['region'])
            from_city = (test_return[i]['from']['city'])
            home_country = (test_return[i]['home']['country'])
            home_region = (test_return[i]['home']['region'])
            home_city = (test_return[i]['home']['city'])
            if birth_date == "" and cnt_flag != 'R':
                cnt_flag = 'R'
            if passport == "" and cnt_flag != 'R':
                cnt_flag = 'R'

            # Checking format of passport
            valid_passport_format(passport)
            if valid_passport_format_flag == False and cnt_flag != 'R':
                cnt_flag = 'R'
            if last_name == "" and cnt_flag != 'R':
                cnt_flag = 'R'
            if first_name == "" and cnt_flag != 'R':
                cnt_flag = 'R'
            if entry_reason == "" and cnt_flag != 'R':
                cnt_flag = 'R'
            if entry_reason.lower() == 'visiting':
                visa_code = (test_return[i]['visa_code'])
                visa_date = (test_return[i]['visa_date'])
                visit_visa_check(from_country, COUNTRIES)
                if visit_visa_check_flag:
                    valid_visa_format(visa_code)
                    if not valid_visa_format_flag and cnt_flag != 'R':
                        cnt_flag = 'R'
                    valid_date_format(visa_date)
                    if not valid_date_format_flag and cnt_flag != 'R':
                        cnt_flag = 'R'
                    is_more_than_x_years_ago(2,visa_date)
                    if not x_years_flag and cnt_flag != 'R':
                        cnt_flag = 'R'
            if from_country == "" and cnt_flag != 'R':
                cnt_flag = 'R'
            if from_region == "" and cnt_flag != 'R':
                cnt_flag = 'R'
            if from_city == "" and cnt_flag != 'R':
                cnt_flag = 'R'

            # Decision for Question 2
            location_check(from_country, COUNTRIES)
            if location_check_flag == 'R' and cnt_flag != 'R':
                cnt_flag = 'R'

            # Decision for Question 5
            medical_advisory_check(from_country, COUNTRIES)
            if medical_advisory_check_flag == 'Q' and cnt_flag != 'R':
                cnt_flag = 'Q'
            if home_country == "" and cnt_flag != 'R':
                cnt_flag = 'R'
            if home_region == "" and cnt_flag != 'R':
                cnt_flag = 'R'
            if home_city == "" and cnt_flag != 'R':
                cnt_flag = 'R'

            # Decision for Question 3
            if home_country.upper() == 'KAN' and cnt_flag == 'F':
                cnt_flag = 'A'

            # If any of the above checks return 'Reject' the entry record will be rejected
            if cnt_flag != 'F':
                if cnt_flag == 'R':
                    list.append("Reject")
                elif cnt_flag == 'Q':
                    list.append("Quarantine")
                else:
                    list.append("Accept")
                cnt_flag = 'F'
            i = i + 1
            continue 
        return list
    
##if __name__ == "__main__":
##    # execute only if run as a script
##    main()
##p = location_check('LUG', COUNTRIES)
##print(p)
