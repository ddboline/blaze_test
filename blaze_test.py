#!/usr/bin/python

import os
from sqlalchemy import create_engine
import pandas as pd

USER = os.getenv('USER')

def blaze_test():
    engine = create_engine('postgresql://ddboline:BQGIvkKFZPejrKvX@localhost/lahman2014')
    con = engine.connect()

if __name__ == '__main__':
    blaze_test()
