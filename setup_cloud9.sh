#!/bin/bash

sudo apt-get update

sudo bash -c "echo deb ssh://ddboline@ddbolineathome.mooo.com/var/www/html/deb/trusty ./ > /etc/apt/sources.list.d/py2deb2.list"
sudo apt-get update
sudo apt-get install -y --force-yes postgresql-client python-psycopg2 g++ python-dev \
                                    ipython python-blaze python-pandas \
                                    python-cytoolz python-theano python-lasagne \
                                    python-nolearn python-pylearn2 python-sqlalchemy

git clone https://github.com/ContinuumIO/blaze
