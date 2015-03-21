#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--my-foo', default='foobar')
parser.add_argument('-b', '--bar-value', default=3.14)
args = parser.parse_args()
print args.f
#print "pinging path ", args.s
#answer = args.x**args.y
#print args.my_foo
