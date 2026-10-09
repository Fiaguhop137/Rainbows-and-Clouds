#!/bin/bash
while pgrep -f 'prism\.py' >/dev/null; do
    pkill -f 'prism\.py'
done
nohup python3 prism.py > prism.log 2>&1 &