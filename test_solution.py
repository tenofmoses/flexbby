import pytest
from solution import check_passport_date

def test_passport_is_valid():
    assert check_passport_date('10/01/2015', '14.12.2000') == True

def test_passport_is_valid_2():
    assert check_passport_date('10/11/2012', '14.12.1987') == True

def test_passport_is_valid_3():
    assert check_passport_date('15/06/2017', '14.05.1972') == True

def test_passport_is_valid_4():
    assert check_passport_date('10/12/2016', '14.11.1971') == True


def test_passport_is_not_valid():
    assert check_passport_date('10/01/2015', '14.12.2006') == False

def test_passport_is_not_valid_2():
    assert check_passport_date('20/05/2001', '14.05.1987') == False

def test_passport_is_not_valid_4():
    assert check_passport_date('10/11/2016', '14.11.1971') == False
