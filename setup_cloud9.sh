#!/bin/bash

sudo cp -a ${HOME}/.ssh /root/
sudo chown -R root:root /root/
sudo bash -c "echo deb ssh://ddboline@ddbolineathome.mooo.com/var/www/html/deb/trusty/blaze ./ > /etc/apt/sources.list.d/py2deb2.list"
sudo apt-get update
sudo apt-get install -y --force-yes postgresql-client python-psycopg2 g++ \
                                    python-dev ipython python-blaze \
                                    python-scikit-learn python-numpy=1.10\* \
                                    python-coverage 

git clone https://github.com/ContinuumIO/blaze
