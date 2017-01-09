#!/bin/bash

sudo cp -a ${HOME}/.ssh /root/
sudo chown -R root:root /root/
sudo bash -c "echo deb ssh://ddboline@ddbolineathome.mooo.com/var/www/html/deb/xenial/devel ./ > /etc/apt/sources.list.d/py2deb2.list"
sudo apt-get update
sudo apt-get install -y --force-yes postgresql-client python-psycopg2 g++ \
                                    python-sklearn python-numpy=1.\* \
                                    python-setuptools python-pandas \
                                    python-blaze
sudo apt-get install -f -y --force-yes
