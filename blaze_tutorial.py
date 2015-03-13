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
bl_df_dir = dir(df)

df = pd.DataFrame(L, columns=['id', 'name', 'amount'])
print df[df.amount < 0].name
pd_df_dir = dir(df)

print len(bl_df_dir), len(pd_df_dir)
print len([d for d in bl_df_dir if d in pd_df_dir])
print [d for d in bl_df_dir if d not in pd_df_dir]
print [d for d in pd_df_dir if d not in bl_df_dir]

t = Data([(1, 'Alice', 100),
         (2, 'Bob', -200),
         (3, 'Charlie', 300),
         (4, 'Denis', 400),
         (5, 'Edith', -500)],
         fields=['id', 'name', 'balance'])

print t