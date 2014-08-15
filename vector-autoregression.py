#Vector-Autoregression using previous overall scores and average performance in MATH and ELA combined

import MySQLdb
import pandas.io.sql as psql
from pandas import *
import numpy as np
import scipy.stats
import scipy
from sklearn import linear_model
from sklearn import preprocessing

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='password',
    db='school')


df_scores = psql.read_sql('SELECT * FROM allyears_ems', con=mydb)
df_other = psql.read_sql('SELECT * FROM allyears_EMS_other', con=mydb)


df_all = merge(df_scores,df_other,right_on='DBN',left_on='DBN')
df_all['2012_13_PERF'] = (df_all['2012_13_MATH'] + df_all['2012_13_ELA'])/2
df_all['2011_12_PERF'] = (df_all['2011_12_MATH'] + df_all['2011_12_ELA'])/2
df_all['2010_11_PERF'] = (df_all['2010_11_MATH'] + df_all['2010_11_ELA'])/2
df_all['2009_10_PERF'] = (df_all['2009_10_MATH'] + df_all['2009_10_ELA'])/2
df_all['2008_09_PERF'] = (df_all['2008_09_MATH'] + df_all['2008_09_ELA'])/2
df_all['2007_08_PERF'] = (df_all['2007_08_MATH'] + df_all['2007_08_ELA'])/2
df_all['2006_07_PERF'] = (df_all['2006_07_MATH'] + df_all['2006_07_ELA'])/2


model = linear_model.LinearRegression()

X = df_all[['2006_07_SCORE','2007_08_SCORE','2008_09_SCORE','2009_10_SCORE','2010_11_SCORE','2006_07_PERF','2007_08_PERF','2008_09_PERF','2009_10_PERF','2010_11_PERF']]

imputer = preprocessing.Imputer(strategy='median')
imputer.fit(X)
X_imputed = imputer.transform(X)


y = df_all['2011_12_SCORE']
imputer = preprocessing.Imputer(strategy='median',axis = 1)
imputer.fit(y)
y_imputed = imputer.transform(y)

model.fit(X_imputed,np.ravel(y_imputed))
out = model.predict(X_imputed)
#model.score(X_imputed,ravel(y_imputed))

df = df_scores
df_scores['auto_pred_2012'] = DataFrame(out)

RMSE_auto_train = ((df['auto_pred_2012']-df['2011_12_SCORE'])**2).mean()**(0.5)
print "RMSE of autoregression training data: " +  str(RMSE_auto_train)

X_test = df_all[['2007_08_SCORE','2008_09_SCORE','2009_10_SCORE','2010_11_SCORE','2011_12_SCORE','2007_08_PERF','2008_09_PERF','2009_10_PERF','2010_11_PERF','2011_12_PERF']]

imputer = preprocessing.Imputer(strategy='median')
imputer.fit(X_test)
X_test_imputed = imputer.transform(X_test)

y_test = df_all['2012_13_SCORE']
imputer = preprocessing.Imputer(strategy='median',axis = 1)
imputer.fit(y_test)
y_test_imputed = imputer.transform(y_test)

out = model.predict(X_test_imputed)


df['auto_pred_2013'] = DataFrame(out)

RMSE_auto_test = ((df['auto_pred_2013']-df['2012_13_SCORE'])**2).mean()**(0.5)
print "RMSE of vector autoregression on test data: " +  str(RMSE_auto_test)

coef = model.coef_
print "coefficients of autoregression: " + str(coef)

inter = model.intercept_
print "intercept of autoregression: " + str(inter)

d = {'Middle':Series([29.1, 37.3, 53.0, 67.7]),'K-8':Series([32.0, 40.6, 53.2, 63.1]),'Elementary':Series([30.0, 36.5, 48.8, 60.1])}
cut = DataFrame(d)

df['grade_pred_2013'] = Series(np.nan)
df['grade_pred_2013'][(df['auto_pred_2013'] < cut['Middle'][0]) & (df['School_Type'] == 'Middle')] = 'F'
df['grade_pred_2013'][(df['auto_pred_2013'] >= cut['Middle'][0]) & (df['auto_pred_2013'] < cut['Middle'][1]) & (df['School_Type'] == 'Middle')] = 'D'
df['grade_pred_2013'][(df['auto_pred_2013'] >= cut['Middle'][1]) & (df['auto_pred_2013'] < cut['Middle'][2]) & (df['School_Type'] == 'Middle')] = 'C'
df['grade_pred_2013'][(df['auto_pred_2013'] >= cut['Middle'][2]) & (df['auto_pred_2013'] < cut['Middle'][3]) & (df['School_Type'] == 'Middle')] = 'B'
df['grade_pred_2013'][(df['auto_pred_2013'] >= cut['Middle'][3]) & (df['School_Type'] == 'Middle')] = 'A'


df['grade_pred_2013'][(df['auto_pred_2013'] < cut['K-8'][0]) & (df['School_Type'] == 'K-8')] = 'F'
df['grade_pred_2013'][(df['auto_pred_2013'] >= cut['K-8'][0]) & (df['auto_pred_2013'] < cut['K-8'][1]) & (df['School_Type'] == 'K-8')] = 'D'
df['grade_pred_2013'][(df['auto_pred_2013'] >= cut['K-8'][1]) & (df['auto_pred_2013'] < cut['K-8'][2]) & (df['School_Type'] == 'K-8')] = 'C'
df['grade_pred_2013'][(df['auto_pred_2013'] >= cut['K-8'][2]) & (df['auto_pred_2013'] < cut['K-8'][3]) & (df['School_Type'] == 'K-8')] = 'B'
df['grade_pred_2013'][(df['auto_pred_2013'] >= cut['K-8'][3]) & (df['School_Type'] == 'K-8')] = 'A'


df['grade_pred_2013'][(df['auto_pred_2013'] < cut['Elementary'][0]) & (df['School_Type'] == 'Elementary')] = 'F'
df['grade_pred_2013'][(df['auto_pred_2013'] >= cut['Elementary'][0]) & (df['auto_pred_2013'] < cut['Elementary'][1]) & (df['School_Type'] == 'Elementary')] = 'D'
df['grade_pred_2013'][(df['auto_pred_2013'] >= cut['Elementary'][1]) & (df['auto_pred_2013'] < cut['Elementary'][2]) & (df['School_Type'] == 'Elementary')] = 'C'
df['grade_pred_2013'][(df['auto_pred_2013'] >= cut['Elementary'][2]) & (df['auto_pred_2013'] < cut['Elementary'][3]) & (df['School_Type'] == 'Elementary')] = 'B'
df['grade_pred_2013'][(df['auto_pred_2013'] >= cut['Elementary'][3]) & (df['School_Type'] == 'Elementary')] = 'A'


conv_dict={'A':5.,'B':4.,'C':3.,'D':2.,'F':1,'None':np.nan}
df.head()
df_grade = df[['DBN','School','School_Type']]
df_grade['2012_13_GRADE'] = df['2012_13_GRADE'].apply(conv_dict.get)
df_grade['grade_pred_2013'] = df['grade_pred_2013'].apply(conv_dict.get)


RMSE_grade = ((df_grade['2012_13_GRADE']-df_grade['grade_pred_2013'])**2).mean()**(0.5)
print RMSE_grade




