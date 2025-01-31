from helpers import  run_python_script

import sys
import os

from code.packaging import parse_packaging, calc_total_units, get_unit

def test_should_pass():
    print("This will always pass!")
    assert True

def test_parse_packaging():    
    # tests the package parser
    tests = [
        ("12 eggs in 1 carton", [{ 'eggs' : 12}, {'carton' : 1}]),
        ("6 bars in 1 pack / 12 packs in 1 carton", [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]),
        ("20 pieces in 1 pack / 10 packs in 1 carton / 4 cartons in 1 box", [{ 'pieces' : 20}, {'packs' : 10}, {'cartons' : 4}, {'box' : 1}]),
        ("2 foo in 1 bar / 3 bars in 1 baz / 4 baz in 1 qux / 2 qux in 1 biz ", [{ 'foo' : 2}, {'bars' : 3}, {'baz' : 4}, {'qux' : 2}, {'biz' : 1}]),
        ("25 balls in 1 bucket / 4 buckets in 1 bin", [{'balls' : 25}, {'buckets' : 4}, {'bin' : 1}]),
    ]

    for text, expected in tests:
        print(f"Testing: {text}")
        print(f"EXPECTED: {expected}")
        actual = parse_packaging(text) 
        print(f"ACTUAL  : {actual}")
        assert actual == expected

def test_calc_total_units():
    # tests the total units in the package
    tests = [
        ([{ 'eggs' : 12}, {'carton' : 1}], 12),
        ([{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}], 72),
        ([{ 'pieces' : 20}, {'packs' : 10}, {'cartons' : 4}, {'box' : 1}], 800),
        ([{ 'foo' : 2}, {'bars' : 3}, {'baz' : 4}, {'qux' : 2}, {'biz' : 1}], 48),
        ([{'balls' : 25}, {'buckets' : 4}, {'bin' : 1}], 100)
    ]

    for package, expected in tests:
        print(f"Testing: {package}")
        print(f"EXPECTED: {expected}")
        actual = calc_total_units(package) 
        print(f"ACTUAL  : {actual}")
        assert actual == expected

def test_get_unit():
    # tests getting the unit
    tests = [
        ([{ 'eggs' : 12}, {'carton' : 1}], 'eggs'),
        ([{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}], 'bars'),
        ([{ 'pieces' : 20}, {'packs' : 10}, {'cartons' : 4}, {'box' : 1}], 'pieces'),
        ([{ 'foo' : 2}, {'bars' : 3}, {'baz' : 4}, {'qux' : 2}, {'biz' : 1}], 'foo'),
        ([{'balls' : 25}, {'buckets' : 4}, {'bin' : 1}], 'balls')
    ]

    for package, expected in tests:
        print(f"Testing: {package}")
        print(f"EXPECTED: {expected}")
        actual = get_unit(package) 
        print(f"ACTUAL  : {actual}")
        assert actual == expected
