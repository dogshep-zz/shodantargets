#!/usr/bin/python

# imports

import shodan
import sys
import argparse

# debug

debug = 1

# keys

SHODAN_API_KEY = "x"
api = shodan.Shodan(SHODAN_API_KEY)

# parse arguments

parser = argparse.ArgumentParser()
parser.add_argument("-sterm", "-s", help="search for a string on shodan")
parser.add_argument("-outputfile", "-o", help="output file location")
args = parser.parse_args()
file = args.outputfile

# shodan search

output = []
try:
	results = api.search(args.sterm)
	
	print 'Results found: %s' % results['total']
	for result in results['matches']:
#		print 'IP: %s' % result['ip_str']
		output.append(' %s' % result['ip_str'])
except shodan.APIError, e:
	print 'Error: %s' % e

# output to file

f = open(file, "w")
newlist = ''.join(output)
f.write(newlist)
f.close()

# success

print '%s written successfully.' % args.outputfile
