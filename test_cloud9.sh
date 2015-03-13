#!/bin/bash

if [ "$HOSTNAME" != "dilepton-tower" ]; then
    ssh -N -L 5432:localhost:5432 ddboline@ddbolineathome.mooo.com &
fi

./blaze_test.py
./blaze_tutorial.py
