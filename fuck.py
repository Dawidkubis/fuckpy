#!/usr/bin/python

from sys import argv
import argparse
from os import path

parser = argparse.ArgumentParser("Brainfuck interpreter")
parser.add_argument("file")
#parser.add_argument("-i", help="run in interactive mode")
args = parser.parse_args()

# read the file
content = open(args.file).read()

# initialize memory
memory = [0]
index = 0

# is debug? TODO
#debug = len(argv) > 2 and argv[2] in ("-d", --debug) 
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
		pass
		# TODO loops
	elif c == "]":
		pass

