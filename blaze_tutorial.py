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

print repr(iris.head())

iris = bl.transform(iris, sepal_ratio=iris.sepal_length/iris.sepal_width, petal_ratio=iris.petal_length/iris.petal_width)
print repr(iris.head())

print repr(iris.like(species='*versicolor'))

print repr(iris.relabel(petal_length='PETAL-LENGTH', petal_width='PETAL-WIDTH'))

pd_df = pd.DataFrame({
   'name': ['Alice', 'Bob', 'Joe', 'Bob'],
   'amount': [100, 200, 300, 400],
   'id': [1, 2, 3, 4],
})

# put the `df` DataFrame into a Blaze Data object
bl_df = bl.DataFrame(pd_df)
bl_dt = bl.Data(pd_df)

print repr(pd_df.amount * 2)
print repr(bl_df.amount * 2)
print repr(bl_dt.amount * 2)

print repr(pd_df[['id', 'amount']])
print repr(bl_df[['id', 'amount']])
print repr(bl_dt[['id', 'amount']])

print repr(pd_df[pd_df.amount > 300])
print repr(bl_df[bl_df.amount > 300])
print repr(bl_dt[bl_dt.amount > 300])

print repr(pd_df.groupby('name').amount.mean())
print repr(pd_df.groupby(['name', 'id']).amount.mean())

print repr(bl_df.groupby('name').amount.mean())
print repr(bl_df.groupby(['name', 'id']).amount.mean())

print repr(bl.by(bl_dt.name, amount=bl_dt.amount.mean()))
print repr(bl.by(bl.merge(bl_dt.name, bl_dt.id), amount=bl_dt.amount.mean()))

#pd.merge(pd_df, pd_df2, on='name')
#bl.join(bl_dt, bl_dt2, 'name')

print repr(pd_df.amount.map(lambda x: x+1))
print repr(bl_df.amount.map(lambda x: x+1))
print repr(bl_dt.amount.map(lambda x: x+1, 'int64'))

print repr(pd_df.rename(columns={'name': 'alias', 'amount': 'dollars'}))
print repr(bl_df.rename(columns={'name': 'alias', 'amount': 'dollars'}))
print repr(bl_dt.relabel(name='alias', amount='dollars'))

print repr(pd_df.drop_duplicates())
print repr(bl_df.drop_duplicates())
print repr(bl_dt.distinct())

print repr(pd_df.name.drop_duplicates())
print repr(bl_df.name.drop_duplicates())
print repr(bl_dt.name.distinct())

print repr(pd_df.amount.mean())
print repr(bl_df.amount.mean())
print repr(bl_dt.amount.mean())

print repr(pd_df)
print repr(bl_df)
print repr(bl_dt)

print repr(pd_df.amount.value_counts())
print repr(bl_df.amount.value_counts())
print repr(bl_dt.amount.count_values())

print repr(pd_df.dtypes)
print repr(bl_df.dtypes)
print repr(bl_dt.dshape)

print repr(pd_df.amount.dtypes)
print repr(bl_df.amount.dtypes)
print repr(bl_dt.amount.dshape)

print type(pd_df), type(bl_df), type(bl_dt)

