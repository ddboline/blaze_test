#!/usr/bin/python

import os
from sqlalchemy import create_engine
import pandas as pd
import blaze as bl
import into

USER = os.getenv('USER')

def blaze_test():
    engine = create_engine('postgresql://ddboline:BQGIvkKFZPejrKvX@192.168.0.100:5432/lahman2014')
    db = bl.Data(engine)
    print dir(db)
    df = db.teams.columns

if __name__ == '__main__':
    blaze_test()
