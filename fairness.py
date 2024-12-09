#!/usr/bin/python3

import os
import time

os.system("make reset")
os.system("make delay1")

os.system("iperf3 -c 172.31.62.26 -t 60 -p 5201 -A 1 -l 1M > node1.txt &")

time.sleep(5)

os.system("iperf3 -c 172.31.62.26 -t 60 -p 5200 -A 1 -l 1M > node2.txt &")
os.system("make reset")
os.system("make delay2")

time.sleep(5)

os.system("iperf3 -c 172.31.62.26 -t 60 -p 5202 -A 1 -l 1M > node3.txt &")
os.system("make reset")
os.system("make delay3")

time.sleep(5)

os.system("iperf3 -c 172.31.62.26 -t 60 -p 5203 -A 1 -l 1M > node4.txt &")
os.system("make reset")
os.system("make delay4")
