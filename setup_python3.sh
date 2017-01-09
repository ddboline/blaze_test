#!/bin/bash

### hack...
export LANG="C.UTF-8"

sudo bash -c "echo deb ssh://ddboline@ddbolineathome.mooo.com/var/www/html/deb/xenial/python3/devel ./ > /etc/apt/sources.list.d/py2deb2.list"
sudo apt-get update
sudo apt-get install -y --force-yes postgresql-client python3-psycopg2 g++ \
                                    python3-dev python3-blaze \
                                    python3-sklearn python3-numpy=1.\* \
                                    python3-pandas
sudo apt-get install -f -y --force-yes

git clone https://github.com/ContinuumIO/blaze
