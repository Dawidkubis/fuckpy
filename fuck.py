#!/usr/bin/python

from sys import argv
from os import path


# read the file
content = open(argv[1]).read()

# initialize memory
memory = [0]
index = 0

# is debug?
debug = len(argv) > 2 and argv[2] in ("-d", --debug) 
# TODO proper argument handling
# TODO debug
# TODO interactive mode

# lexical analysis and parsing
# (at the same time)
for c in content:
	if c == ">":
		index += 1

		# allocating memory dynamically
		if index >= len(memory):
			memory.append(0)
	elif c == "<":
		# leaving it seeing as
		# it adds additional
		# functionality
		index -= 1
	elif c == "+":
		memory[index] += 1
	elif c == "-":
		memory[index] -= 1
	elif c == ".":
		print(chr(memory[index]))
	elif c == ",":
		memory[index] = ord(input("> ")[0])
	elif c == "[":
		# TODO loops
	elif c == "]":

