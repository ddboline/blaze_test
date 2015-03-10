#!/bin/bash

sudo apt-get install -y postgresql-client
sudo apt-get install -y python-psycopg2
sudo apt-get install -y python-sqlalchemy python-sqlalchemy-ext

sudo bash -c "echo deb http://ddbolineathome.mooo.com/deb/trusty ./ > /etc/apt/sources.list.d/py2deb.list"
sudo apt-get update
sudo apt-get install -y --force-yes ipython python-blaze python-theano python-lasagne python-nolearn python-pylearn2
