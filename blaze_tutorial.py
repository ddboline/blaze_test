#!/usr/bin/python

import os
from sqlalchemy import create_engine
import pandas as pd
import blaze as bl

accounts = bl.Symbol('accounts', 'var * {id: int, name: string, amount: int}')
deadbeats = accounts[accounts.amount < 0].name

L = [[1, 'Alice',   100],
     [2, 'Bob',    -200],
     [3, 'Charlie', 300],
     [4, 'Denis',   400],
     [5, 'Edith',  -500]]

print list(bl.compute(deadbeats, L))

df = bl.DataFrame(L, columns=['id', 'name', 'amount'])
print bl.compute(deadbeats, df)
print dir(df)
