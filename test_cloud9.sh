#!/bin/bash

./blaze_test.py > test.out
./blaze_tutorial.py > tutorial.out

md5sum test.out tutorial.out
