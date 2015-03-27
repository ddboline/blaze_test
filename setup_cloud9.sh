#!/bin/bash

sudo apt-get update
sudo apt-get install -y postgresql-client
sudo apt-get install -y python-psycopg2
sudo apt-get install -y g++ python-dev

sudo bash -c "echo deb ssh://ddboline@ddbolineathome.mooo.com/var/www/html/deb/trusty ./ > /etc/apt/sources.list.d/py2deb2.list"
sudo apt-get update
sudo apt-get install -y --force-yes ipython python-blaze
sudo apt-get install -y --force-yes python-pandas
sudo apt-get install -y --force-yes python-theano python-lasagne 
sudo apt-get install -y --force-yes python-nolearn python-pylearn2
sudo apt-get install -y --force-yes python-sqlalchemy

git clone https://github.com/ContinuumIO/blaze
