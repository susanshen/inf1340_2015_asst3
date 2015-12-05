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

DIR = "test_jsons/"
os.chdir(DIR)


def test_returning():
    """
    Travellers are returning to KAN.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]


def entry_record_check_complete(input_file):
    """
    Entry Record is complete.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]


def entry_record_check_incomplete(input_file):
    """
    First entry record is incomplete.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Reject", "Accept", "Quarantine"]


def unknown_location(input_file):
    """
    Entry record location is unknown.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Reject", "Accept", "Quarantine"]


def medical_advisory(input_file):
    """
    Traveling through country with medical advisory.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Reject", "Accept", "Quarantine"]