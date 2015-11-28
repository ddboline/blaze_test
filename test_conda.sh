#!/bin/bash

python3 ./blaze_test.py > test.out
python3 ./blaze_tutorial.py > tutorial.out

md5sum test.out tutorial.out

