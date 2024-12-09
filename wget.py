#!/usr/bin/python3

import os
import time

os.system("touch data.txt")

# os.system("taskset -c 1 wget -r -np -k 172.31.62.26:5000 &")

while True:
    os.system("taskset -c 0 ss -iHO dst 172.31.62.26 >> data.txt")
    time.sleep(0.1)
# Ctrl-C to stop collecting data
