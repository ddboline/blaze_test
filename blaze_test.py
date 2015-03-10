#!/usr/bin/python

import os
from sqlalchemy import create_engine
import pandas as pd
import blaze as bl
import into

USER = os.getenv('USER')

def blaze_test():
    db = bl.Data('postgresql://ddboline:BQGIvkKFZPejrKvX@192.168.0.100:5432/lahman2014')
    for d in dir(db):
        if hasattr(db, d):
            if type(getattr(db, d)) == bl.expr.expressions.Field:
                print d, type(getattr(db, d))
    df = db.teams
    print df.columns
    into.into('temp_*.csv', 'postgresql://ddboline:BQGIvkKFZPejrKvX@192.168.0.100:5432/lahman2014')

if __name__ == '__main__':
    blaze_test()
