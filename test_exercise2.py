#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

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


#def test_returning():
#    """
#    Travellers are returning to KAN.
#    """
#    assert decide("test_returning_citizen.json", "countries.json") ==\
#        ["Accept", "Accept", "Quarantine"]


#def test_entry_record_completeness():
#    """
#    Traveller's entry record has incomplete required information
#    """
#    assert decide("test_returning_citizen_2.json", "countries.json") ==\
#        ["Reject", "Accept", "Quarantine"]


def test_location_existence():
    """
    Location mentioned in entry record is unknown
    """
    assert decide("test_returning_citizen_3.json", "countries.json") ==\
        ["Accept", "Accept", "Reject"]


def test_visa_existence():
    """
   Reason for entry is to visit and the visitor has a passport from a country from which a visitor visa is required.
   But the traveller does not have a visa.
    """
    assert decide("test_returning_citizen_4.json", "countries.json") ==\
        ["Reject", "Accept", "Quarantine"]


def test_visa_validation():
    """
   Reason for entry is to visit and the visitor has a passport from a country from which a visitor visa is required.
   And the traveller has a valid visa.
    """
    assert decide("test_returning_citizen_5.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]


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