#!/bin/bash

sudo apt-get install -y postgresql-client
sudo apt-get install -y python-psycopg2

sudo bash -c "echo deb https://ddbolineathome.mooo.com/deb/trusty ./ > /etc/apt/sources.list.d/py2deb.list"
sudo apt-get update
sudo apt-get install -y --force-yes ipython python-blaze
sudo apt-get install -y --force-yes python-pandas
sudo apt-get install -y --force-yes python-theano python-lasagne 
sudo apt-get install -y --force-yes python-nolearn python-pylearn2
sudo apt-get install -y --force-yes python-sqlalchemy
