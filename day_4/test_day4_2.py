import pytest

from day_4.day4_2 import *


@pytest.mark.parametrize("val,expected", [
    ("0", False),
    ("-1", False),
    ("1919", False),
    ("1920", True),
    ("1921", True),
    ("2001", True),
    ("2002", True),
    ("2003", False),
])
def test_is_valid_byr(val, expected):
    assert is_valid_byr(val) == expected


@pytest.mark.parametrize("val,expected", [
    ("0", False),
    ("-1", False),
    ("2009", False),
    ("2010", True),
    ("2011", True),
    ("2019", True),
    ("2020", True),
    ("2021", False),
])
def test_is_valid_iyr(val, expected):
    assert is_valid_iyr(val) == expected


@pytest.mark.parametrize("val,expected", [
    ("0", False),
    ("-1", False),
    ("2019", False),
    ("2020", True),
    ("2021", True),
    ("2029", True),
    ("2030", True),
    ("2031", False),
])
def test_is_valid_eyr(val, expected):
    assert is_valid_eyr(val) == expected


@pytest.mark.parametrize("val,expected", [
    ("0", False),
    ("-1", False),
    ("-1cm", False),
    ("-150cm", False),
    ("149cm", False),
    ("150cm", True),
    ("151cm", True),
    ("192cm", True),
    ("193cm", True),
    ("194cm", False),
    ("58in", False),
    ("59in", True),
    ("60in", True),
    ("75in", True),
    ("76in", True),
    ("77in", False)
])
def test_is_valid_hgt(val, expected):
    assert is_valid_hgt(val) == expected


@pytest.mark.parametrize("val,expected", [
    ("#123abc", True),
    ("#000000", True),
    ("#ffffff", True),
    ("#999999", True),
    ("#aaaaaa", True),
    ("abc123", False),
    ("#aaaaag", False),
    ("#aaaaaz", False)
])
def test_is_valid_hcl(val, expected):
    assert is_valid_hcl(val) == expected


@pytest.mark.parametrize("val,expected", [
    ("amb", True),
    ("blu", True),
    ("brn", True),
    ("gry", True),
    ("grn", True),
    ("hzl", True),
    ("oth", True),
    ("amb ", False),
    ("wat", False)
])
def test_is_valid_ecl(val, expected):
    assert is_valid_ecl(val) == expected


@pytest.mark.parametrize("val,expected", [
    ("000000000", True),
    ("123456789", True),
    ("999999999", True),
    ("010101010", True),
    (" 00300000", False),
    ("002000000 ", False),
    (" 010000000", False)
])
def test_is_valid_pid(val, expected):
    assert is_valid_pid(val) == expected


