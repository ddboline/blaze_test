#!/usr/bin/python
""" Tests for blaze """
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os
import shlex
import time
from subprocess import Popen
import pandas as pd
import blaze as bl
import odo


USER = os.getenv('USER')
HOSTNAME = os.uname()[1]


def blaze_test(port=5432):
    user = 'ddboline'
    pwd = 'BQGIvkKFZPejrKvX'
    host = 'localhost'
    dbname = 'lahman2014'
    dbstring = 'postgresql://%s:%s@%s:%s/%s' % (user, pwd, host, port, dbname)
    dbb = bl.Data(dbstring)
    tables = []
    for dbc in dir(dbb):
        if hasattr(dbb, dbc):
            if type(getattr(dbb, dbc)) == bl.expr.expressions.Field:
                tables.append(dbc)
    teams_df = dbb.teams
    print(teams_df.columns)
    for tab in tables:
        csvstr = '%s.csv' % tab
        print(tab)
        teams_df = odo.odo(getattr(dbb, tab), pd.DataFrame)
        odo.odo(teams_df, bl.CSV(csvstr))
        os.system('gzip %s' % csvstr)
        print(teams_df.describe())
    return


class OpenPostgreSQLsshTunnel(object):
    """ Class to let us open an ssh tunnel, then close it when done """
    def __init__(self, port=5432):
        self.tunnel_process = 0
        self.postgre_port = 5432
        self.remote_port = port

    def __enter__(self):
        if HOSTNAME != 'dilepton-tower':
            self.postgre_port = self.remote_port
            _cmd = 'ssh -N -L localhost:%d' % self.remote_port + \
                   ':localhost:5432 ddboline@ddbolineathome.mooo.com'
            args = shlex.split(_cmd)
            self.tunnel_process = Popen(args, shell=False)
            time.sleep(5)
        return self.postgre_port

    def __exit__(self, exc_type, exc_value, traceback):
        if self.tunnel_process:
            self.tunnel_process.kill()
        if exc_type or exc_value or traceback:
            return False
        else:
            return True


if __name__ == '__main__':
    with OpenPostgreSQLsshTunnel(port=5433) as pport:
        blaze_test(port=pport)
