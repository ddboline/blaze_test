#!/usr/bin/python
""" Tests for blaze """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import pandas as pd
import blaze as bl
import odo

USER = os.getenv('USER')


def blaze_test():
    user = 'ddboline'
    pwd = 'BQGIvkKFZPejrKvX'
#    host = 'ddbolineathome.mooo.com'
    host = 'localhost'
    port = 5432
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

if __name__ == '__main__':
    blaze_test()
