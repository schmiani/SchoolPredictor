
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
df['median_indiv_pred'] = df[['2011_12_SCORE','2010_11_SCORE','2009_10_SCORE','2008_09_SCORE','2007_08_SCORE','2006_07_SCORE']].median(1)
df['mean_indiv_pred'] = df[['2011_12_SCORE','2010_11_SCORE','2009_10_SCORE','2008_09_SCORE','2007_08_SCORE','2006_07_SCORE']].mean(1)

n = df.shape[0]

RMSE_mean = ((df['2012_13_SCORE'].mean()-df['2012_13_SCORE'])**2).mean()**(0.5)
print "RMSE for mean score: " + str(RMSE_mean)

RMSE_last = ((df['last_pred']-df['2012_13_SCORE'])**2).mean()**(0.5)
print "RMSE for using last years score: " + str(RMSE_last)

last_notnull_perc = (df['last_pred']-df['2012_13_SCORE']).count()/float(df.shape[0])
print str(last_notnull_perc) + "% not Null"

RMSE_median_indiv = ((df['median_indiv_pred']-df['2012_13_SCORE'])**2).mean()**(0.5)
print "RMSE for using median over previous years: " +  str(RMSE_median_indiv)

median_indiv_notull_perc = (df['median_indiv_pred']-df['2012_13_SCORE']).count()/float(df.shape[0])
print str(median_indiv_notull_perc) + "% not Null"

RMSE_mean_indiv = ((df['mean_indiv_pred']-df['2012_13_SCORE'])**2).mean()**(0.5)
print "RMSE for using mean over previous years: " +  str(RMSE_mean_indiv)

mean_indiv_notull_perc = (df['mean_indiv_pred']-df['2012_13_SCORE']).count()/float(df.shape[0])
print str(mean_indiv_notull_perc) + "% not Null"


df['std'] = df[['2012_13_SCORE','2011_12_SCORE','2010_11_SCORE','2009_10_SCORE','2008_09_SCORE','2007_08_SCORE','2006_07_SCORE']].std(1)

df['2012_13_GRADE_PRED'] = Series(np.nan)

d = {'Middle':Series([29.1, 37.3, 53.0, 67.7]),'K-8':Series([32.0, 40.6, 53.2, 63.1]),'Elementary':Series([30.0, 36.5, 48.8, 60.1])}
cut = DataFrame(d)

df['2012_13_GRADE_PRED'][(df['last_pred'] < cut['Middle'][0]) & (df['School_Type'] == 'Middle')] = 'F'
df['2012_13_GRADE_PRED'][(df['last_pred'] >= cut['Middle'][0]) & (df['last_pred'] < cut['Middle'][1]) & (df['School_Type'] == 'Middle')] = 'D'
df['2012_13_GRADE_PRED'][(df['last_pred'] >= cut['Middle'][1]) & (df['last_pred'] < cut['Middle'][2]) & (df['School_Type'] == 'Middle')] = 'C'
df['2012_13_GRADE_PRED'][(df['last_pred'] >= cut['Middle'][2]) & (df['last_pred'] < cut['Middle'][3]) & (df['School_Type'] == 'Middle')] = 'B'
df['2012_13_GRADE_PRED'][(df['last_pred'] >= cut['Middle'][3]) & (df['School_Type'] == 'Middle')] = 'A'


df['2012_13_GRADE_PRED'][(df['last_pred'] < cut['K-8'][0]) & (df['School_Type'] == 'K-8')] = 'F'
df['2012_13_GRADE_PRED'][(df['last_pred'] >= cut['K-8'][0]) & (df['last_pred'] < cut['K-8'][1]) & (df['School_Type'] == 'K-8')] = 'D'
df['2012_13_GRADE_PRED'][(df['last_pred'] >= cut['K-8'][1]) & (df['last_pred'] < cut['K-8'][2]) & (df['School_Type'] == 'K-8')] = 'C'
df['2012_13_GRADE_PRED'][(df['last_pred'] >= cut['K-8'][2]) & (df['last_pred'] < cut['K-8'][3]) & (df['School_Type'] == 'K-8')] = 'B'
df['2012_13_GRADE_PRED'][(df['last_pred'] >= cut['K-8'][3]) & (df['School_Type'] == 'K-8')] = 'A'

df['2012_13_GRADE_PRED'][(df['last_pred'] < cut['Elementary'][0]) & (df['School_Type'] == 'Elementary')] = 'F'
df['2012_13_GRADE_PRED'][(df['last_pred'] >= cut['Elementary'][0]) & (df['last_pred'] < cut['Elementary'][1]) & (df['School_Type'] == 'Elementary')] = 'D'
df['2012_13_GRADE_PRED'][(df['last_pred'] >= cut['Elementary'][1]) & (df['last_pred'] < cut['Elementary'][2]) & (df['School_Type'] == 'Elementary')] = 'C'
df['2012_13_GRADE_PRED'][(df['last_pred'] >= cut['Elementary'][2]) & (df['last_pred'] < cut['Elementary'][3]) & (df['School_Type'] == 'Elementary')] = 'B'
df['2012_13_GRADE_PRED'][(df['last_pred'] >= cut['Elementary'][3]) & (df['School_Type'] == 'Elementary')] = 'A'

conv_dict={'A':5.,'B':4.,'C':3.,'D':2.,'F':1,'None':np.nan}
df.head()
df_grade = df[['DBN','School','School_Type']]
df_grade['2012_13_GRADE'] = df['2012_13_GRADE'].apply(conv_dict.get)
df_grade['2012_13_GRADE_PRED'] = df['2012_13_GRADE_PRED'].apply(conv_dict.get)

RMSE_grade = ((df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED'])**2).mean()**(0.5)
print RMSE_grade

print 'Gardes correct for last grade: '+str(sum((df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 0)/float(df['2012_13_GRADE'].count()))
print 'Gardes 1 off for last grade: '+str(sum((df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 1)/float(df['2012_13_GRADE'].count()))
print 'Gardes 2 off for last grade: '+str(sum((df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 2)/float(df['2012_13_GRADE'].count()))
print 'Gardes 3 off for last grade: '+str(sum((df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 3)/float(df['2012_13_GRADE'].count()))
print 'Gardes 4 off for last grade: '+str(sum((df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 4)/float(df['2012_13_GRADE'].count()))



df['2012_13_GRADE_PRED'][(df['mean_indiv_pred'] < cut['Middle'][0]) & (df['School_Type'] == 'Middle')] = 'F'
df['2012_13_GRADE_PRED'][(df['mean_indiv_pred'] >= cut['Middle'][0]) & (df['mean_indiv_pred'] < cut['Middle'][1]) & (df['School_Type'] == 'Middle')] = 'D'
df['2012_13_GRADE_PRED'][(df['mean_indiv_pred'] >= cut['Middle'][1]) & (df['mean_indiv_pred'] < cut['Middle'][2]) & (df['School_Type'] == 'Middle')] = 'C'
df['2012_13_GRADE_PRED'][(df['mean_indiv_pred'] >= cut['Middle'][2]) & (df['mean_indiv_pred'] < cut['Middle'][3]) & (df['School_Type'] == 'Middle')] = 'B'
df['2012_13_GRADE_PRED'][(df['mean_indiv_pred'] >= cut['Middle'][3]) & (df['School_Type'] == 'Middle')] = 'A'


df['2012_13_GRADE_PRED'][(df['mean_indiv_pred'] < cut['K-8'][0]) & (df['School_Type'] == 'K-8')] = 'F'
df['2012_13_GRADE_PRED'][(df['mean_indiv_pred'] >= cut['K-8'][0]) & (df['mean_indiv_pred'] < cut['K-8'][1]) & (df['School_Type'] == 'K-8')] = 'D'
df['2012_13_GRADE_PRED'][(df['mean_indiv_pred'] >= cut['K-8'][1]) & (df['mean_indiv_pred'] < cut['K-8'][2]) & (df['School_Type'] == 'K-8')] = 'C'
df['2012_13_GRADE_PRED'][(df['mean_indiv_pred'] >= cut['K-8'][2]) & (df['mean_indiv_pred'] < cut['K-8'][3]) & (df['School_Type'] == 'K-8')] = 'B'
df['2012_13_GRADE_PRED'][(df['mean_indiv_pred'] >= cut['K-8'][3]) & (df['School_Type'] == 'K-8')] = 'A'

df['2012_13_GRADE_PRED'][(df['mean_indiv_pred'] < cut['Elementary'][0]) & (df['School_Type'] == 'Elementary')] = 'F'
df['2012_13_GRADE_PRED'][(df['mean_indiv_pred'] >= cut['Elementary'][0]) & (df['mean_indiv_pred'] < cut['Elementary'][1]) & (df['School_Type'] == 'Elementary')] = 'D'
df['2012_13_GRADE_PRED'][(df['mean_indiv_pred'] >= cut['Elementary'][1]) & (df['mean_indiv_pred'] < cut['Elementary'][2]) & (df['School_Type'] == 'Elementary')] = 'C'
df['2012_13_GRADE_PRED'][(df['mean_indiv_pred'] >= cut['Elementary'][2]) & (df['mean_indiv_pred'] < cut['Elementary'][3]) & (df['School_Type'] == 'Elementary')] = 'B'
df['2012_13_GRADE_PRED'][(df['mean_indiv_pred'] >= cut['Elementary'][3]) & (df['School_Type'] == 'Elementary')] = 'A'

conv_dict={'A':5.,'B':4.,'C':3.,'D':2.,'F':1,'None':np.nan}
df.head()
df_grade = df[['DBN','School','School_Type']]
df_grade['2012_13_GRADE'] = df['2012_13_GRADE'].apply(conv_dict.get)
df_grade['2012_13_GRADE_PRED'] = df['2012_13_GRADE_PRED'].apply(conv_dict.get)

RMSE_grade = ((df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED'])**2).mean()**(0.5)
print RMSE_grade

print 'Gardes correct for mean over pervious grades: '+str(sum((df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 0)/float(df['2012_13_GRADE'].count()))
print 'Gardes 1 off for mean over pervious grades: '+str(sum((df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 1)/float(df['2012_13_GRADE'].count()))
print 'Gardes 2 off for mean over pervious grades: '+str(sum((df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 2)/float(df['2012_13_GRADE'].count()))
print 'Gardes 3 off for mean over pervious grades: '+str(sum((df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 3)/float(df['2012_13_GRADE'].count()))
print 'Gardes 4 off for mean over pervious grades: '+str(sum((df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 4)/float(df['2012_13_GRADE'].count()))

