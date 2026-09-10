#!/bin/bash
while pgrep -f 'cirrus\.py' >/dev/null; do
    pkill -9 -f 'cirrus\.py'
done
nohup python3 cirrus.py > cirrus.log 2>&1 &