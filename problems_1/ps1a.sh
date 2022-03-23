#!/usr/bin/env bash

printf "120000\n.10\n1000000" | python3 ps1a.py
echo "Expected: 183"
echo

python3 ps1a.py <<e
80000
.15
500000
e
echo "Expected: 105"
echo
