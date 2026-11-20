"""
Tests for comfort_level() based on its equivalence classes.

Assumes comfort_level() is in a file called weather.py in the same folder.
Run with:  pytest -v
"""
from weather import comfort_level


# COLD class: temperature <= 15.0
def test_cold_typical():
    assert comfort_level(0.0) == "COLD"


def test_cold_negative():
    assert comfort_level(-10.0) == "COLD"


def test_cold_boundary():
    assert comfort_level(15.0) == "COLD"      # 15.0 itself is COLD


# OK class: 15.0 < temperature <= 25.0
def test_ok_just_above_cold_boundary():
    assert comfort_level(15.1) == "OK"


def test_ok_typical():
    assert comfort_level(20.0) == "OK"


def test_ok_boundary():
    assert comfort_level(25.0) == "OK"        # 25.0 itself is OK


# HOT class: temperature > 25.0
def test_hot_just_above_boundary():
    assert comfort_level(25.1) == "HOT"


def test_hot_typical():
    assert comfort_level(30.0) == "HOT"
