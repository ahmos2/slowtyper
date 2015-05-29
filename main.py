import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(float(1)/float(60))
while True:
    for fName in sys.argv[1:]:
        f=open(fName)
        delay_print(f.read())
        f.close()
        time.sleep(10)
        sys.stdout.write("\x1b[2J\x1b[H") #Clear screen
