#!/bin/bash

sudo apt-get update

sudo bash -c "echo deb ssh://ddboline@ddbolineathome.mooo.com/var/www/html/deb/trusty/devel ./ > /etc/apt/sources.list.d/py2deb2.list"
sudo apt-get update
sudo apt-get install -y --force-yes postgresql-client python-psycopg2 g++ \
                                    python-dev ipython python-blaze python-scikit-learn

git clone https://github.com/ContinuumIO/blaze
