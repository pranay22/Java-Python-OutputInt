#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse

def main():
	# initialize command line argument parser
	parser = argparse.ArgumentParser(description="Test script to be used as a template for connecting Patho and Java Script with argparse")
	parser.add_argument("-a", "--aarg", help="argument a", action="store", required=True)
	parser.add_argument("-b", "--barg", help="argument b", action="store", required=False)
	parser.add_argument("-c", "--carg", help="argument c", action="store", required=False)
	
	var_b = None
	bar_c = None
	args = parser.parse_args()
	var_a = args.aarg
	if (args.barg):
		var_b = args.barg
	if (args.carg):
		var_c = args.carg
	print ("Inside Python script to be invoked form inside Java script")
	print ("Variable a:" + var_a)
	if (args.barg):
		print ("Variable b:" + var_b)
	if (args.carg):
		print ("Variable c:" + var_c)
	sys.stdout.flush()

# call the main method
if __name__=="__main__":
	main()
