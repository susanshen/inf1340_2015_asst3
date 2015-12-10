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
#from exercise2 import visit_visa_check

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




#def medical_advisory():

 #   assert visit_visa_check("test_returning_citizen.json", "countries.json") ==\
  #      [True]