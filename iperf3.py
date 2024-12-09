#!/usr/bin/python3

import os
import time

os.system("touch data.txt")

os.system("iperf3 -c 172.31.62.26 -t 60 -p 5201 -A 1 -l 1M &")

while True:
    os.system("taskset -c 0 ss -iHO dst 172.31.62.26 >> data.txt")
    time.sleep(0.1)
# Ctrl-C to stop collecting data
