
#Simple predictions for scores of Elementary, K-8 and Middle Schools
import MySQLdb
import pandas.io.sql as psql
from pandas import *
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='password',
    db='school')

df_mysql = psql.read_sql('SELECT * FROM allyears_EMS', con=mydb)

fig = plt.figure()
df_mysql['2012_13_SCORE'].hist()
fig.savefig('2012_13_score_hist.png')

fig = plt.figure()
df_mysql['2011_12_SCORE'].hist()
fig.savefig('2011_12_score_hist.png')

fig = plt.figure()
df_mysql['2010_11_SCORE'].hist()
fig.savefig('2010_11_score_hist.png')

fig = plt.figure()
df_mysql['2009_10_SCORE'].hist()
fig.savefig('2009_10_score_hist.png')

fig = plt.figure()
df_mysql['2008_09_SCORE'].hist()
fig.savefig('2008_09_score_hist.png')

fig = plt.figure()
df_mysql['2007_08_SCORE'].hist()
fig.savefig('2007_08_score_hist.png')

fig = plt.figure()
df_mysql['2006_07_SCORE'].hist()
fig.savefig('2006_07_score_hist.png')


df = df_mysql

df['last_pred'] = df['2011_12_SCORE']

df['median_pred'] = df['2011_12_SCORE'].median()

df['median_indiv_pred'] = df[['2011_12_SCORE','2010_11_SCORE','2009_10_SCORE','2008_09_SCORE','2007_08_SCORE','2006_07_SCORE']].median(1)

RMSE_median = ((df['median_pred']-df['2012_13_SCORE'])**2).mean()**(0.5)
RMSE_median

n = df.shape[0]
n

median_notnull_perc = (df['median_pred']-df['2012_13_SCORE']).count()/float(df.shape[0])
median_notnull_perc

RMSE_last = ((df['last_pred']-df['2012_13_SCORE'])**2).mean()**(0.5)
RMSE_last

last_notnull_perc = (df['last_pred']-df['2012_13_SCORE']).count()/float(df.shape[0])
last_notnull_perc

RMSE_median_indiv = ((df['median_indiv_pred']-df['2012_13_SCORE'])**2).mean()**(0.5)
RMSE_median_indiv

median_indiv_notull_perc = (df['median_indiv_pred']-df['2012_13_SCORE']).count()/float(df.shape[0])
median_indiv_notull_perc


df['std'] = df[['2012_13_SCORE','2011_12_SCORE','2010_11_SCORE','2009_10_SCORE','2008_09_SCORE','2007_08_SCORE','2006_07_SCORE']].std(1)

