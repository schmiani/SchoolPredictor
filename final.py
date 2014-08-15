#Vector-autoregression with custom imputing:
#For rows with some data, use median over row.
#For rows with no data in one class (score or performance), uses median over population (before imputing on rows)

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

df_all = merge(df_scores,df_other)
df_all['2012_13_PERF'] = (df_all['2012_13_MATH'] + df_all['2012_13_ELA'])/2
df_all['2011_12_PERF'] = (df_all['2011_12_MATH'] + df_all['2011_12_ELA'])/2
df_all['2010_11_PERF'] = (df_all['2010_11_MATH'] + df_all['2010_11_ELA'])/2
df_all['2009_10_PERF'] = (df_all['2009_10_MATH'] + df_all['2009_10_ELA'])/2
df_all['2008_09_PERF'] = (df_all['2008_09_MATH'] + df_all['2008_09_ELA'])/2
df_all['2007_08_PERF'] = (df_all['2007_08_MATH'] + df_all['2007_08_ELA'])/2
df_all['2006_07_PERF'] = (df_all['2006_07_MATH'] + df_all['2006_07_ELA'])/2


X_all = df_all[['2006_07_SCORE','2007_08_SCORE','2008_09_SCORE','2009_10_SCORE','2010_11_SCORE','2011_12_SCORE','2012_13_SCORE','2006_07_PERF','2007_08_PERF','2008_09_PERF','2009_10_PERF','2010_11_PERF','2011_12_PERF','2012_13_PERF']]
medians = X_all.median()

X_imputed = X_all.copy()
for index,row in X_imputed.iterrows():
    if row[:7].isnull().sum()==7:
        X_imputed.iloc[index,0:7] = medians[:7]
    elif row[:7].isnull().sum()>0:
        ind = row[:7][row[:7].isnull() == True].index.tolist()
        X_imputed[index:index+1][ind] = row[:7].median()
    if row[7:16].isnull().sum()==7:
        X_imputed.iloc[index,7:] = medians[7:]
    elif row[7:16].isnull().sum()>0:
        ind = row[7:16][row[7:16].isnull() == True].index.tolist()
        X_imputed[index:index+1][ind] = row[7:16].median()


model = linear_model.LinearRegression()

X_train = X_imputed[['2006_07_SCORE','2007_08_SCORE','2008_09_SCORE','2009_10_SCORE','2010_11_SCORE','2006_07_PERF','2007_08_PERF','2008_09_PERF','2009_10_PERF','2010_11_PERF']]
y_train = X_imputed['2011_12_SCORE']

model.fit(X_train,y_train)
out = model.predict(X_train)

df = df_scores
df_scores['2011_12_SCORE_PRED'] = DataFrame(out)

RMSE_auto_train = ((df['2011_12_SCORE_PRED']-df['2011_12_SCORE'])**2).mean()**(0.5)
print "RMSE of autoregression training data: " +  str(RMSE_auto_train)

X_test = X_imputed[['2007_08_SCORE','2008_09_SCORE','2009_10_SCORE','2010_11_SCORE','2011_12_SCORE','2007_08_PERF','2008_09_PERF','2009_10_PERF','2010_11_PERF','2011_12_PERF']]
y_test = X_imputed['2012_13_SCORE']

out = model.predict(X_test)
df['2012_13_SCORE_PRED'] = DataFrame(out)

RMSE_auto_test = ((df['2012_13_SCORE_PRED']-df['2012_13_SCORE'])**2).mean()**(0.5)
print "RMSE of vector autoregression on test data: " +  str(RMSE_auto_test)

coef = model.coef_
print "coefficients of autoregression: " + str(coef)

inter = model.intercept_
print "intercept of autoregression: " + str(inter)

d = {'Middle':Series([29.1, 37.3, 53.0, 67.7]),'K-8':Series([32.0, 40.6, 53.2, 63.1]),'Elementary':Series([30.0, 36.5, 48.8, 60.1])}
cut = DataFrame(d)

df['grade_pred_2013'] = Series(np.nan)

df['grade_pred_2013'][(df['2012_13_SCORE_PRED'] < cut['Middle'][0]) & (df['School_Type'] == 'Middle')] = 'F'
df['grade_pred_2013'][(df['2012_13_SCORE_PRED'] >= cut['Middle'][0]) & (df['2012_13_SCORE_PRED'] < cut['Middle'][1]) & (df['School_Type'] == 'Middle')] = 'D'
df['grade_pred_2013'][(df['2012_13_SCORE_PRED'] >= cut['Middle'][1]) & (df['2012_13_SCORE_PRED'] < cut['Middle'][2]) & (df['School_Type'] == 'Middle')] = 'C'
df['grade_pred_2013'][(df['2012_13_SCORE_PRED'] >= cut['Middle'][2]) & (df['2012_13_SCORE_PRED'] < cut['Middle'][3]) & (df['School_Type'] == 'Middle')] = 'B'
df['grade_pred_2013'][(df['2012_13_SCORE_PRED'] >= cut['Middle'][3]) & (df['School_Type'] == 'Middle')] = 'A'


df['grade_pred_2013'][(df['2012_13_SCORE_PRED'] < cut['K-8'][0]) & (df['School_Type'] == 'K-8')] = 'F'
df['grade_pred_2013'][(df['2012_13_SCORE_PRED'] >= cut['K-8'][0]) & (df['2012_13_SCORE_PRED'] < cut['K-8'][1]) & (df['School_Type'] == 'K-8')] = 'D'
df['grade_pred_2013'][(df['2012_13_SCORE_PRED'] >= cut['K-8'][1]) & (df['2012_13_SCORE_PRED'] < cut['K-8'][2]) & (df['School_Type'] == 'K-8')] = 'C'
df['grade_pred_2013'][(df['2012_13_SCORE_PRED'] >= cut['K-8'][2]) & (df['2012_13_SCORE_PRED'] < cut['K-8'][3]) & (df['School_Type'] == 'K-8')] = 'B'
df['grade_pred_2013'][(df['2012_13_SCORE_PRED'] >= cut['K-8'][3]) & (df['School_Type'] == 'K-8')] = 'A'

df['grade_pred_2013'][(df['2012_13_SCORE_PRED'] < cut['Elementary'][0]) & (df['School_Type'] == 'Elementary')] = 'F'
df['grade_pred_2013'][(df['2012_13_SCORE_PRED'] >= cut['Elementary'][0]) & (df['2012_13_SCORE_PRED'] < cut['Elementary'][1]) & (df['School_Type'] == 'Elementary')] = 'D'
df['grade_pred_2013'][(df['2012_13_SCORE_PRED'] >= cut['Elementary'][1]) & (df['2012_13_SCORE_PRED'] < cut['Elementary'][2]) & (df['School_Type'] == 'Elementary')] = 'C'
df['grade_pred_2013'][(df['2012_13_SCORE_PRED'] >= cut['Elementary'][2]) & (df['2012_13_SCORE_PRED'] < cut['Elementary'][3]) & (df['School_Type'] == 'Elementary')] = 'B'
df['grade_pred_2013'][(df['2012_13_SCORE_PRED'] >= cut['Elementary'][3]) & (df['School_Type'] == 'Elementary')] = 'A'

conv_dict={'A':5.,'B':4.,'C':3.,'D':2.,'F':1,'None':np.nan}
df.head()
df_grade = df[['DBN','School','School_Type']]
df_grade['2012_13_GRADE'] = df['2012_13_GRADE'].apply(conv_dict.get)
df_grade['grade_pred_2013'] = df['grade_pred_2013'].apply(conv_dict.get)


RMSE_grade = ((df_grade['2012_13_GRADE']-df_grade['grade_pred_2013'])**2).mean()**(0.5)
print RMSE_grade


model.fit(X_test,y_test)
out = model.predict(X_test)

df_scores['2012_13_SCORE_PRED'] = DataFrame(out)

RMSE_auto_final = ((df['2012_13_SCORE_PRED']-df['2012_13_SCORE'])**2).mean()**(0.5)
print "RMSE of autoregression final data: " +  str(RMSE_auto_final)

X_final = X_imputed[['2008_09_SCORE','2009_10_SCORE','2010_11_SCORE','2011_12_SCORE','2012_13_SCORE','2008_09_PERF','2009_10_PERF','2010_11_PERF','2011_12_PERF','2012_13_PERF']]

out = model.predict(X_final)
df_scores['2013_14_SCORE_PRED'] = DataFrame(out)

coef = model.coef_
print "coefficients of autoregression: " + str(coef)

inter = model.intercept_
print "intercept of autoregression: " + str(inter)

df['2013_14_GRADE_PRED'] = Series(np.nan)

df['2013_14_GRADE_PRED'][(df['2013_14_SCORE_PRED'] < cut['Middle'][0]) & (df['School_Type'] == 'Middle')] = 'F'
df['2013_14_GRADE_PRED'][(df['2013_14_SCORE_PRED'] >= cut['Middle'][0]) & (df['2013_14_SCORE_PRED'] < cut['Middle'][1]) & (df['School_Type'] == 'Middle')] = 'D'
df['2013_14_GRADE_PRED'][(df['2013_14_SCORE_PRED'] >= cut['Middle'][1]) & (df['2013_14_SCORE_PRED'] < cut['Middle'][2]) & (df['School_Type'] == 'Middle')] = 'C'
df['2013_14_GRADE_PRED'][(df['2013_14_SCORE_PRED'] >= cut['Middle'][2]) & (df['2013_14_SCORE_PRED'] < cut['Middle'][3]) & (df['School_Type'] == 'Middle')] = 'B'
df['2013_14_GRADE_PRED'][(df['2013_14_SCORE_PRED'] >= cut['Middle'][3]) & (df['School_Type'] == 'Middle')] = 'A'

df['2013_14_GRADE_PRED'][(df['2013_14_SCORE_PRED'] < cut['K-8'][0]) & (df['School_Type'] == 'K-8')] = 'F'
df['2013_14_GRADE_PRED'][(df['2013_14_SCORE_PRED'] >= cut['K-8'][0]) & (df['2013_14_SCORE_PRED'] < cut['K-8'][1]) & (df['School_Type'] == 'K-8')] = 'D'
df['2013_14_GRADE_PRED'][(df['2013_14_SCORE_PRED'] >= cut['K-8'][1]) & (df['2013_14_SCORE_PRED'] < cut['K-8'][2]) & (df['School_Type'] == 'K-8')] = 'C'
df['2013_14_GRADE_PRED'][(df['2013_14_SCORE_PRED'] >= cut['K-8'][2]) & (df['2013_14_SCORE_PRED'] < cut['K-8'][3]) & (df['School_Type'] == 'K-8')] = 'B'
df['2013_14_GRADE_PRED'][(df['2013_14_SCORE_PRED'] >= cut['K-8'][3]) & (df['School_Type'] == 'K-8')] = 'A'

df['2013_14_GRADE_PRED'][(df['2013_14_SCORE_PRED'] < cut['Elementary'][0]) & (df['School_Type'] == 'Elementary')] = 'F'
df['2013_14_GRADE_PRED'][(df['2013_14_SCORE_PRED'] >= cut['Elementary'][0]) & (df['2013_14_SCORE_PRED'] < cut['Elementary'][1]) & (df['School_Type'] == 'Elementary')] = 'D'
df['2013_14_GRADE_PRED'][(df['2013_14_SCORE_PRED'] >= cut['Elementary'][1]) & (df['2013_14_SCORE_PRED'] < cut['Elementary'][2]) & (df['School_Type'] == 'Elementary')] = 'C'
df['2013_14_GRADE_PRED'][(df['2013_14_SCORE_PRED'] >= cut['Elementary'][2]) & (df['2013_14_SCORE_PRED'] < cut['Elementary'][3]) & (df['School_Type'] == 'Elementary')] = 'B'
df['2013_14_GRADE_PRED'][(df['2013_14_SCORE_PRED'] >= cut['Elementary'][3]) & (df['School_Type'] == 'Elementary')] = 'A'

df['2006_07_PERF_PERC'] = Series(np.nan)
df['2006_07_PERF_PERC'][df_all['School_Type']=='Middle'] = 100*df_all['2006_07_PERF'][df_all['School_Type']=='Middle'].rank()/df_all['2006_07_PERF'][df_all['School_Type']=='Middle'].count()
df['2006_07_PERF_PERC'][df_all['School_Type']=='K-8'] = 100*df_all['2006_07_PERF'][df_all['School_Type']=='K-8'].rank()/df_all['2006_07_PERF'][df_all['School_Type']=='K-8'].count()
df['2006_07_PERF_PERC'][df_all['School_Type']=='Elementary'] = 100*df_all['2006_07_PERF'][df_all['School_Type']=='Elementary'].rank()/df_all['2006_07_PERF'][df_all['School_Type']=='Elementary'].count()
df['2007_08_PERF_PERC'] = Series(np.nan)
df['2007_08_PERF_PERC'][df_all['School_Type']=='Middle'] = 100*df_all['2007_08_PERF'][df_all['School_Type']=='Middle'].rank()/df_all['2007_08_PERF'][df_all['School_Type']=='Middle'].count()
df['2007_08_PERF_PERC'][df_all['School_Type']=='K-8'] = 100*df_all['2007_08_PERF'][df_all['School_Type']=='K-8'].rank()/df_all['2007_08_PERF'][df_all['School_Type']=='K-8'].count()
df['2007_08_PERF_PERC'][df_all['School_Type']=='Elementary'] = 100*df_all['2007_08_PERF'][df_all['School_Type']=='Elementary'].rank()/df_all['2007_08_PERF'][df_all['School_Type']=='Elementary'].count()
df['2008_09_PERF_PERC'] = Series(np.nan)
df['2008_09_PERF_PERC'][df_all['School_Type']=='Middle'] = 100*df_all['2008_09_PERF'][df_all['School_Type']=='Middle'].rank()/df_all['2008_09_PERF'][df_all['School_Type']=='Middle'].count()
df['2008_09_PERF_PERC'][df_all['School_Type']=='K-8'] = 100*df_all['2008_09_PERF'][df_all['School_Type']=='K-8'].rank()/df_all['2008_09_PERF'][df_all['School_Type']=='K-8'].count()
df['2008_09_PERF_PERC'][df_all['School_Type']=='Elementary'] = 100*df_all['2008_09_PERF'][df_all['School_Type']=='Elementary'].rank()/df_all['2008_09_PERF'][df_all['School_Type']=='Elementary'].count()
df['2009_10_PERF_PERC'] = Series(np.nan)
df['2009_10_PERF_PERC'][df_all['School_Type']=='Middle'] = 100*df_all['2009_10_PERF'][df_all['School_Type']=='Middle'].rank()/df_all['2009_10_PERF'][df_all['School_Type']=='Middle'].count()
df['2009_10_PERF_PERC'][df_all['School_Type']=='K-8'] = 100*df_all['2009_10_PERF'][df_all['School_Type']=='K-8'].rank()/df_all['2009_10_PERF'][df_all['School_Type']=='K-8'].count()
df['2009_10_PERF_PERC'][df_all['School_Type']=='Elementary'] = 100*df_all['2009_10_PERF'][df_all['School_Type']=='Elementary'].rank()/df_all['2009_10_PERF'][df_all['School_Type']=='Elementary'].count()
df['2010_11_PERF_PERC'] = Series(np.nan)
df['2010_11_PERF_PERC'][df_all['School_Type']=='Middle'] = 100*df_all['2010_11_PERF'][df_all['School_Type']=='Middle'].rank()/df_all['2010_11_PERF'][df_all['School_Type']=='Middle'].count()
df['2010_11_PERF_PERC'][df_all['School_Type']=='K-8'] = 100*df_all['2010_11_PERF'][df_all['School_Type']=='K-8'].rank()/df_all['2010_11_PERF'][df_all['School_Type']=='K-8'].count()
df['2010_11_PERF_PERC'][df_all['School_Type']=='Elementary'] = 100*df_all['2010_11_PERF'][df_all['School_Type']=='Elementary'].rank()/df_all['2010_11_PERF'][df_all['School_Type']=='Elementary'].count()
df['2011_12_PERF_PERC'] = Series(np.nan)
df['2011_12_PERF_PERC'][df_all['School_Type']=='Middle'] = 100*df_all['2011_12_PERF'][df_all['School_Type']=='Middle'].rank()/df_all['2011_12_PERF'][df_all['School_Type']=='Middle'].count()
df['2011_12_PERF_PERC'][df_all['School_Type']=='K-8'] = 100*df_all['2011_12_PERF'][df_all['School_Type']=='K-8'].rank()/df_all['2011_12_PERF'][df_all['School_Type']=='K-8'].count()
df['2011_12_PERF_PERC'][df_all['School_Type']=='Elementary'] = 100*df_all['2011_12_PERF'][df_all['School_Type']=='Elementary'].rank()/df_all['2011_12_PERF'][df_all['School_Type']=='Elementary'].count()
df['2012_13_PERF_PERC'] = Series(np.nan)
df['2012_13_PERF_PERC'][df_all['School_Type']=='Middle'] = 100*df_all['2012_13_PERF'][df_all['School_Type']=='Middle'].rank()/df_all['2012_13_PERF'][df_all['School_Type']=='Middle'].count()
df['2012_13_PERF_PERC'][df_all['School_Type']=='K-8'] = 100*df_all['2012_13_PERF'][df_all['School_Type']=='K-8'].rank()/df_all['2012_13_PERF'][df_all['School_Type']=='K-8'].count()
df['2012_13_PERF_PERC'][df_all['School_Type']=='Elementary'] = 100*df_all['2012_13_PERF'][df_all['School_Type']=='Elementary'].rank()/df_all['2012_13_PERF'][df_all['School_Type']=='Elementary'].count()


df_final = df[['DBN','School','School_Type','2013_14_SCORE_PRED','2013_14_GRADE_PRED',\
'2012_13_SCORE','2012_13_GRADE','2011_12_SCORE','2011_12_GRADE','2010_11_SCORE','2010_11_GRADE','2009_10_SCORE','2009_10_GRADE','2008_09_SCORE','2008_09_GRADE','2007_08_SCORE','2007_08_GRADE','2006_07_SCORE','2006_07_GRADE',\
'2012_13_PERF_PERC','2011_12_PERF_PERC','2010_11_PERF_PERC','2009_10_PERF_PERC','2008_09_PERF_PERC','2007_08_PERF_PERC','2006_07_PERF_PERC']]
ddf_final = df_final.fillna(value='')

df_final.to_csv('./data/dump_final.csv')