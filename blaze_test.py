#!/usr/bin/python

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
    print teams_df.columns
    for tab in tables:
        csvstr = '%s.csv' % tab
        print tab
        odo.odo(getattr(dbb, tab), bl.CSV(csvstr))
        os.system('gzip %s' % csvstr)
        teams_df = pd.read_csv('%s.gz' % csvstr, compression='gzip')
        print teams_df.describe()
        exit(0)

if __name__ == '__main__':
    blaze_test()
