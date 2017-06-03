#!/usr/bin/env python
import time
import sys
import argparse

def delay_print(string, charsPerSecond):
    for character in string:
        sys.stdout.write( '%s' % character )
        sys.stdout.flush()
        time.sleep(float(1)/float(charsPerSecond))

parser = argparse.ArgumentParser(description='Type out files slowly')
parser.add_argument('-o', '--once', default=False, dest='once', action='store_true', help='Only go through file-list once')
parser.add_argument('-s', '--speed', default=60, type=int, help='Characters per second')
parser.add_argument('-w', '--wait', default=10, type=int, help='Wait between files')
parser.add_argument('files', metavar='filename', type=str, nargs='+', help='Files to print out')
args = parser.parse_args()

while True:
    for fName in args.files:
        f=open(fName)
        delay_print(f.read(), args.speed)
        f.close()
        time.sleep(10)
        sys.stdout.write("\x1b[2J\x1b[H") #Clear screen
    if args.once:
        break
