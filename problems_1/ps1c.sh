#!/usr/bin/env bash

python3 ps1c.py <<e
150000
e
echo "Expected: 0.4411 and 12"
echo

python3 ps1c.py <<e
300000
e
echo "Expected: 0.2206 and 9"
echo

python3 ps1c.py <<e
10000
e
echo "Expected: \"It is not possible to pay the down payment in three years.\""
echo
