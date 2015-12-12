#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = 'Deanna Wong, Alyha Shahrukh & Susan Shen'
__email__ = "deanna.wong@mail.utoronto.ca, alyha.shahrukh@mail.utoronto.ca & shuyun.shen@mail.utoronto.ca"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import pytest
import os
from exercise2 import decide
from exercise2 import valid_visa_format
from exercise2 import valid_date_format
from exercise2 import valid_passport_format
DIR = "test_jsons/"
os.chdir(DIR)


def test_returning():
    """
    Travellers are returning to KAN.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]


def test_case_sensitivity():
    """
    Travellers are returning to KAN. Country code and passport number correctness is checked.
    """
    assert decide("test_returning_citizen_2.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]


#def test_entry_record_completeness():
#    """
#    Traveller's entry record completeness is checked when they are returning or visiting a country.
#    """
#    assert decide("test_entry_record_completeness.json", "countries.json") ==\
#        ["Reject", "Accept", "Reject"]


def test_number_of_records_1():
    """
    A JSON input file has more than 3 entry records.
    """
    assert decide("test_number_of_records.json", "countries.json") ==\
        ["Reject", "Accept", "Reject", "Accept"]


def test_number_of_records_2():
    """
    A JSON input file has less than 3 entry records.
    """
    assert decide("test_number_of_records_2.json", "countries.json") ==\
        ["Reject", "Accept"]


def test_location_existence():
    """
    Traveller's home country and the country the traveller came from is checked to see if the country exists
    when they are returning or visiting a country.
    """
    assert decide("test_location_existence.json", "countries.json") ==\
        ["Accept", "Accept", "Reject"]


def test_visa_existence():
    """
   When reason for entry is to visit and the visitor has a passport from a country from which a visitor
   visa is required, it is required to check if traveller has a visa or not.
    """
    assert decide("test_visa_existence.json", "countries.json") ==\
        ["Accept", "Reject", "Quarantine"]


def test_visa_validation():
    """
    When reason for entry is to visit, the visitor has a passport from a country from which a visitor visa is required,
    and visitor has a visa, it is required to check if the visa is valid or not.
    """
    assert decide("test_visa_validation.json", "countries.json") ==\
        ["Reject", "Accept", "Reject"]


def test_medical_advisory_check():
    """
    Traveller is coming from or travelling through a country with a medical advisory.
    """
    assert decide("test_medical_advisory_check.json", "countries.json") ==\
        ["Quarantine", "Accept", "Quarantine"]


def test_valid_visa_format():
    assert valid_visa_format("i8fue-si4kf") == True


def test_invalid_visa_format_1():
    """
   Testing invalid visa format due to missing characters
    """
    assert valid_visa_format("ifue-si4kf") == False


def test_invalid_visa_format_2():
    """
   Testing invalid visa format due to the inclusion of symbols rather than numbers or letters
    """
    assert valid_visa_format("&&&&&-si4kf") == False


def test_valid_date_format():
    assert valid_date_format("2014-09-08") == True


def test_invalid_date_format_1():
    """
   Testing invalid date format due to missing digit
    """
    assert valid_date_format("2014-09-0") == False


def test_invalid_date_format_2():
    """
   Testing invalid date format due to inclusion of other characters other than numbers
    """
    assert valid_date_format("2014-09-0h") == False


def test_valid_passport_format():
    assert valid_passport_format("gdg7w-w8djw-wjskd-837ed-9wj9d") == True


def test_invalid_passport_format_1():
    """
   Testing invalid passport format due to missing characters
    """
    assert valid_passport_format("gdg7w-w8djw-wjskd-837ed-") == False


def test_invalid_passport_format_2():
    """
   Testing invalid passport format due to the inclusion of symbols rather than numbers or letters
    """
    assert valid_passport_format("gdg7w-w8djw-wjskd-837ed-!!!!!") == False