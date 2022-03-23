#!/usr/bin/env bash

python3 ps1b.py <<e
120000
.05
500000
.03
e
echo "Expected: 142"
echo

python3 ps1b.py <<e
80000
.1
800000
.03
e
echo "Expected: 159"
echo

python3 ps1b.py <<e
75000
.05
1500000
.05
e
echo "Expected: 261"
echo
