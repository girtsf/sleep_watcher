#!/usr/bin/python

import subprocess
import sys
import time

SLEEP_TIME = 10

def Watch(cmd):
    start = time.time()
    while True:
        time.sleep(SLEEP_TIME)
        now = time.time()
        delta = now - start
        if delta > (SLEEP_TIME + 5):
            subprocess.call(cmd, shell=True)
        start = now


if __name__ == '__main__':
    Watch(sys.argv[1])


