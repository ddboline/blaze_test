#!/bin/bash

if [ "$HOSTNAME" != "dilepton-tower" ]; then
    ssh -N -L localhost:5432:localhost:5432 ddboline@ddbolineathome.mooo.com &
    sleep 5
fi

python3 ./blaze_test.py
python3 ./blaze_tutorial.py
