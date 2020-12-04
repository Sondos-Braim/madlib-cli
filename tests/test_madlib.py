from madlib_cli.madlib import read_template
from madlib_cli.madlib import parse
from madlib_cli.madlib import merge

def test_read_template():
    actual=read_template('assets/test.txt')
    expected='This is a test\nhello\nwelcome'
    assert actual == expected

def test_parse():
    string='This is a test for the {second} function which is supposed to return an {array} and a string'
    arr=['second','array']
    actual=parse(string,arr)
    expected="This is a test for the {} function which is supposed to return an {} and a string",['second','array']
    assert actual == expected

def test_merge():
    string='The {} is very {}.'
    arr=['car','fast']
    actual=merge(string,arr)
    expected='The car is very fast.'
    assert actual == expected
