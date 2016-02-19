#!/bin/bash

if [ "$HOSTNAME" != "dilepton-tower" ]; then
    ssh -N -L localhost:5432:localhost:5432 ddboline@ddbolineathome.mooo.com &
    sleep 5
fi

./blaze_test.py > test.out
./blaze_tutorial.py > tutorial.out

md5sum test.out tutorial.out

cat test.out tutorial.out
