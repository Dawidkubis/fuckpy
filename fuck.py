#!/usr/bin/python

from sys import argv
from os import path

assert len(sys.argv) < 3, f'invalid number of arguments: {len(sys.argv)}'

if len(sys.arv == 1):
    import interactive
else:
    if path.exists(sys.argv[1]) and path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as f:
            from parse import parse
            print(parse(f))
    else:
        raise AssertionError('problem opening file: {sys.argv[1]}')
