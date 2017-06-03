#!/usr/bin/env python
import time
import sys
import argparse

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(float(1)/float(60))

parser = argparse.ArgumentParser(description='Type out files slowly')
parser.add_argument('files', metavar='filename', type=str, nargs='+', help='Files to print out')
args = parser.parse_args()

while True:
    for fName in args.files:
        f=open(fName)
        delay_print(f.read())
        f.close()
        time.sleep(10)
        sys.stdout.write("\x1b[2J\x1b[H") #Clear screen
