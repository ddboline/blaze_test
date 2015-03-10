#!/usr/bin/python

import os
from sqlalchemy import create_engine
import pandas as pd
import blaze as bl
import into

USER = os.getenv('USER')

def blaze_test():
    dbstring = 'postgresql://ddboline:BQGIvkKFZPejrKvX@192.168.0.100:5432/lahman2014'
    db = bl.Data(dbstring)
    tables = []
    for d in dir(db):
        if hasattr(db, d):
            if type(getattr(db, d)) == bl.expr.expressions.Field:
                tables.append(d)
    df = db.teams
    print df.columns
    for t in tables:
        csvstr = '%s.csv' % t
        print csvstr, tabstr
        into.into(csvstr, getattr(db, t))

if __name__ == '__main__':
    blaze_test()
