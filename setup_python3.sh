#!/bin/bash

sudo cp -a ${HOME}/.ssh /root/
sudo chown -R root:root /root/
sudo bash -c "echo deb ssh://ddboline@ddbolineathome.mooo.com/var/www/html/deb/trusty/python3/devel ./ > /etc/apt/sources.list.d/py2deb2.list"
sudo apt-get update
sudo apt-get install -y --force-yes postgresql-client python3-psycopg2 g++ \
                                    python3-dev ipython3 python3-blaze \
                                    python3-scikit-learn python3-flask

git clone https://github.com/ContinuumIO/blaze
