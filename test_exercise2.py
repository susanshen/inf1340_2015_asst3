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
#from exercise2 import medical_advisory_check

DIR = "test_jsons/"
os.chdir(DIR)


def test_returning():
    """
    Travellers are returning to KAN.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]


def test_entry_record_completeness():
    """
    Traveller's entry record has incomplete required information
    """
    assert decide("test_returning_citizen_2.json", "countries.json") ==\
        ["Reject", "Accept", "Quarantine"]


def test_location_existence():
    """
    Location mentioned in entry record is unknown
    """
    assert decide("test_returning_citizen_3.json", "countries.json") ==\
        ["Accept", "Accept", "Reject"]



# Problem - testing decide function
# it still passes even when I insert Reject in one of the outputs
def check_visa_validation():
    """
    Reason for entry is to visit and the visitor has a passport from a country from which a visitor visa is required
    the traveller has a valid visa.
    """
    assert decide("test_returning_citizen_4.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]


# Problem - tried to test the medical_advisory function
# it still passes even when I insert Reject in one of the outputs
def medical_advisory():

    assert medical_advisory_check("test_returning_citizen.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]