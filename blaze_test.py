#!/usr/bin/python

import os
from sqlalchemy import create_engine
import pandas as pd
import blaze as bl
import into

USER = os.getenv('USER')

def blaze_test():
    db = bl.Data('postgresql://ddboline:BQGIvkKFZPejrKvX@192.168.0.100:5432/lahman2014')
    tables = []
    for d in dir(db):
        if hasattr(db, d):
            if type(getattr(db, d)) == bl.expr.expressions.Field:
                tables.append(d)
    df = db.teams
    print df.columns
    for t in tables:
        into.into('%s.csv' % t, 'postgresql://ddboline:BQGIvkKFZPejrKvX@192.168.0.100:5432/lahman2014::%s' % t)

if __name__ == '__main__':
    blaze_test()
