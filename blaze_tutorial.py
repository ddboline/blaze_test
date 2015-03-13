#!/usr/bin/python

import os
from sqlalchemy import create_engine
import pandas as pd
import blaze as bl
from into import into

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

t = bl.Data([(1, 'Alice', 100),
         (2, 'Bob', -200),
         (3, 'Charlie', 300),
         (4, 'Denis', 400),
         (5, 'Edith', -500)],
         fields=['id', 'name', 'balance'])

print repr(t)
print repr(t[t.balance < 0])

print repr(t[t.balance < 0].name)
print list(t[t.balance < 0].name)

iris = bl.Data('blaze/blaze/examples/data/iris.csv')
print repr(iris)

iris = bl.Data('sqlite:///blaze/blaze/examples/data/iris.db::iris')
print repr(iris)

print repr(bl.by(iris.species, min=iris.petal_width.min(), max=iris.petal_width.max()))

result = bl.by(iris.species, min=iris.petal_width.min(), max=iris.petal_width.max())

print into(bl.DataFrame, result)
print into(pd.DataFrame, result)

print into('output.csv', result)

print repr(iris.sepal_length.mean())
print repr(bl.mean(iris.sepal_length))

print repr(bl.by(iris.species, shortest=iris.petal_length.min(), longest=iris.petal_length.max(), average=iris.petal_length.mean()))