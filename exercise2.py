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

with open("test_jsons/test_returning_citizen.json", "r") as entry_record_reader:
    entry_record_contents = entry_record_reader.read()
    test_return = json.loads(entry_record_contents)

with open("test_jsons/countries.json", "r") as countries_reader:
    countries_contents = countries_reader.read()
    COUNTRIES = json.loads(countries_contents)


# Input parameters
input_file = test_return
countries_file = COUNTRIES
#


def location_check(input_data, countries_file):
    control_flag = "F"
    for key in countries_file:
        if key.lower() == input_data.lower():
            control_flag = "T"
    if control_flag == "F":
        return "Reject"
    else:
        return "Accept"


def visa_check(input_data, countries_file):
    control_flag = "Reject"
    for key in countries_file:
        if key.lower() == input_data.lower():
            if 0 < int(countries_file[key]['visitor_visa_required']) <= 2:
                control_flag = "Accept"
            else:
                control_flag = "Reject"
##                if 0 < int(countries_file[key]['transit_visa_required']) <= 2:
##                    control_flag = "Accept"
##                else:
##                    control_flag = "Reject"
    return (control_flag)


def medical_advisory_check(input_data, countries_file):
    control_flag = "Reject"
    for key in countries_file:
        if key.lower() == input_data.lower():
            if countries_file[key]['medical_advisory'] == "":
                control_flag = "Accept"
            else:
                control_flag = "Quarantine"
    return control_flag


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
    i = 0
    for key1 in input_file:
        print('Record number', i+1)
##        value1 = key1
##        list1 = value1
        try:
##            print(list1)
##            print(test_return[i])
##            list1 in REQUIRED_FIELDS
#########################################################################################################################
            birth_date_flag = 'Accept'
            passport_flag = 'Accept'
            last_name_flag = 'Accept'
            first_name_flag = 'Accept'
            entry_reason_flag = 'Accept'
            from_country_flag = 'Accept'
            from_region_flag = 'Accept'
            from_city_flag = 'Accept'
            home_country_flag = 'Accept'
            home_region_flag = 'Accept'
            home_city_flag = 'Accept'
            valid_date_format_flag = 'Accept'
            valid_passport_format_flag = 'Accept'
            visa_check_flag = 'Accept'

    ##        print('====================================================================')
        ##    print(test_return[0]['birth_date'])
        ##    print(test_return[0]['passport'])
        ##    print(test_return[0]['last_name'])
        ##    print(test_return[0]['first_name'])
        ##    print(test_return[0]['entry_reason'])
        ##    print(test_return[0]['from']['country'])
        ##    print(test_return[0]['from']['region'])
        ##    print(test_return[0]['from']['city'])
        ##    print(test_return[0]['home']['country'])
        ##    print(test_return[0]['home']['region'])
        ##    print(test_return[0]['home']['city'])
        ##    print('====================================================================')
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
    ##        print('birth_date   =',birth_date)
    ##        print('passport     =',passport)
    ##        print('last_name    =',last_name)
    ##        print('first_name   =',first_name)
    ##        print('entry_reason =',entry_reason)
    ##        print('from_country =',from_country)
    ##        print('from_region  =',from_region)
    ##        print('from_city    =',from_city)
    ##        print('home_country =',home_country)
    ##        print('home_region  =',home_region)
    ##        print('home_city    =',home_city)
    ##        print('--------------------------------------------------------------------')

            if birth_date == "":
                birth_date_flag = 'Reject'
            if passport == "":
                passport_flag = 'Reject'
            if last_name == "":
                last_name_flag = 'Reject'
            if first_name == "":
                first_name_flag = 'Reject'
            if entry_reason == "":
                entry_reason_flag = 'Reject'
            if from_country == "":
                from_country_flag = 'Reject'
            if from_region == "":
                from_region_flag = 'Reject'
            if from_city == "":
                from_city_flag = 'Reject'
            if home_country == "":
                home_country_flag = 'Reject'
            if home_region == "":
                home_region_flag = 'Reject'
            if home_city == "":
                home_city_flag = 'Reject'

    ##        print('Start from_location_flag')
            from_location_flag = location_check(from_country, countries_file)
            if home_country.upper() == 'KAN':
                home_location_flag = 'Accept'
            else:
    ##            print('Start home_location_flag')
                home_location_flag = location_check(home_country, countries_file)


    ##        print('Start medical_advisory_check')
            from_med_adv_flag = medical_advisory_check(from_country, countries_file)

    ##        print('Start visa_check')
            if entry_reason.lower() == 'visit':
                visa_check_flag = visa_check(from_country, countries_file)

            if not valid_date_format(birth_date):
                valid_date_format_flag = 'Reject'

            if not valid_passport_format(passport):
                valid_passport_format_flag = 'Reject'


    ##        if birth_date_flag == 'Reject':
    ##            print('Record numner',i+1,'birth_date_flag',birth_date_flag)
    ##        if passport_flag == 'Reject':
    ##            print('Record numner',i+1,'passport_flag',passport_flag)
    ##        if last_name_flag == 'Reject':
    ##            print('Record numner',i+1,'last_name_flag',last_name_flag)
    ##        if first_name_flag == 'Reject':
    ##            print('Record numner',i+1,'first_name_flag',first_name_flag)
    ##        if entry_reason_flag == 'Reject':
    ##            print('Record numner',i+1,'entry_reason_flag',entry_reason_flag)
    ##        if from_country_flag == 'Reject':
    ##            print('Record numner',i+1,'from_country_flag',from_country_flag)
    ##        if from_region_flag == 'Reject':
    ##            print('Record numner',i+1,'from_region_flag',from_region_flag)
    ##        if from_city_flag == 'Reject':
    ##            print('Record numner',i+1,'from_city_flag',from_city_flag)
    ##        if home_country_flag == 'Reject':
    ##            print('Record numner',i+1,'home_country_flag',home_country_flag)
    ##        if home_region_flag == 'Reject':
    ##            print('Record numner',i+1,'home_region_flag',home_region_flag)
    ##        if home_city_flag == 'Reject':
    ##            print('Record numner',i+1,'home_city_flag',home_city_flag)
    ##
    ##        if from_location_flag == 'Reject':
    ##            print('Record numner',i+1,'from_location_flag',from_location_flag)
    ##        if home_location_flag == 'Reject':
    ##            print('Record numner',i+1,'home_location_flag',home_location_flag)
    ##
    ##        if from_med_adv_flag == 'Reject' or from_med_adv_flag == 'Quarantine':
    ##            print('Record numner',i+1,'from_med_adv_flag',from_med_adv_flag)
    ##
    ##        if visa_check_flag == 'Reject':
    ##            print('Record numner',i+1,'visa_check_flag',visa_check_flag)

    ##        if valid_date_format_flag == 'Reject':
    ##            print('Record numner',i+1,'valid_date_format_flag',valid_date_format_flag)
    ##
    ##        if valid_passport_format_flag == 'Reject':
    ##            print('Record numner',i+1,'valid_passport_format_flag',valid_passport_format_flag)

            if valid_passport_format_flag == 'Reject' or valid_date_format_flag == 'Reject' or birth_date_flag == 'Reject' or passport_flag == 'Reject' or last_name_flag == 'Reject' or first_name_flag == 'Reject' or entry_reason_flag == 'Reject' or from_country_flag == 'Reject' or from_region_flag == 'Reject' or from_city_flag == 'Reject' or home_country_flag == 'Reject' or home_region_flag == 'Reject' or home_city_flag == 'Reject' or from_location_flag == 'Reject' or home_location_flag == 'Reject' or from_med_adv_flag == 'Reject' or from_med_adv_flag == 'Reject':
                print('Reject')
            elif from_med_adv_flag == 'Quarantine':
                print('Quarantine')
            else:
                print('Accept')
#########################################################################################################################
        except KeyError:
            print("JSON format is incorrect")

        i += 1
##        print('********************************************************************')

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


decide(input_file, countries_file)
