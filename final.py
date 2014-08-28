#Autoregression with custom imputing:
#For rows with some data, use median over row.
#For rows with no data in one class (score or performance), uses median over population (before imputing on rows)

import MySQLdb
import pandas.io.sql as psql
from pandas import *
import numpy as np
import scipy.stats
import scipy
from sklearn import linear_model

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

df_all['2006_07_PERF_PERC'] = Series(np.nan)
df_all['2006_07_PERF_PERC'][df_all['School_Type']=='Middle'] = 100*df_all['2006_07_PERF'][df_all['School_Type']=='Middle'].rank()/df_all['2006_07_PERF'][df_all['School_Type']=='Middle'].count()
df_all['2006_07_PERF_PERC'][df_all['School_Type']=='K-8'] = 100*df_all['2006_07_PERF'][df_all['School_Type']=='K-8'].rank()/df_all['2006_07_PERF'][df_all['School_Type']=='K-8'].count()
df_all['2006_07_PERF_PERC'][df_all['School_Type']=='Elementary'] = 100*df_all['2006_07_PERF'][df_all['School_Type']=='Elementary'].rank()/df_all['2006_07_PERF'][df_all['School_Type']=='Elementary'].count()
df_all['2007_08_PERF_PERC'] = Series(np.nan)
df_all['2007_08_PERF_PERC'][df_all['School_Type']=='Middle'] = 100*df_all['2007_08_PERF'][df_all['School_Type']=='Middle'].rank()/df_all['2007_08_PERF'][df_all['School_Type']=='Middle'].count()
df_all['2007_08_PERF_PERC'][df_all['School_Type']=='K-8'] = 100*df_all['2007_08_PERF'][df_all['School_Type']=='K-8'].rank()/df_all['2007_08_PERF'][df_all['School_Type']=='K-8'].count()
df_all['2007_08_PERF_PERC'][df_all['School_Type']=='Elementary'] = 100*df_all['2007_08_PERF'][df_all['School_Type']=='Elementary'].rank()/df_all['2007_08_PERF'][df_all['School_Type']=='Elementary'].count()
df_all['2008_09_PERF_PERC'] = Series(np.nan)
df_all['2008_09_PERF_PERC'][df_all['School_Type']=='Middle'] = 100*df_all['2008_09_PERF'][df_all['School_Type']=='Middle'].rank()/df_all['2008_09_PERF'][df_all['School_Type']=='Middle'].count()
df_all['2008_09_PERF_PERC'][df_all['School_Type']=='K-8'] = 100*df_all['2008_09_PERF'][df_all['School_Type']=='K-8'].rank()/df_all['2008_09_PERF'][df_all['School_Type']=='K-8'].count()
df_all['2008_09_PERF_PERC'][df_all['School_Type']=='Elementary'] = 100*df_all['2008_09_PERF'][df_all['School_Type']=='Elementary'].rank()/df_all['2008_09_PERF'][df_all['School_Type']=='Elementary'].count()
df_all['2009_10_PERF_PERC'] = Series(np.nan)
df_all['2009_10_PERF_PERC'][df_all['School_Type']=='Middle'] = 100*df_all['2009_10_PERF'][df_all['School_Type']=='Middle'].rank()/df_all['2009_10_PERF'][df_all['School_Type']=='Middle'].count()
df_all['2009_10_PERF_PERC'][df_all['School_Type']=='K-8'] = 100*df_all['2009_10_PERF'][df_all['School_Type']=='K-8'].rank()/df_all['2009_10_PERF'][df_all['School_Type']=='K-8'].count()
df_all['2009_10_PERF_PERC'][df_all['School_Type']=='Elementary'] = 100*df_all['2009_10_PERF'][df_all['School_Type']=='Elementary'].rank()/df_all['2009_10_PERF'][df_all['School_Type']=='Elementary'].count()
df_all['2010_11_PERF_PERC'] = Series(np.nan)
df_all['2010_11_PERF_PERC'][df_all['School_Type']=='Middle'] = 100*df_all['2010_11_PERF'][df_all['School_Type']=='Middle'].rank()/df_all['2010_11_PERF'][df_all['School_Type']=='Middle'].count()
df_all['2010_11_PERF_PERC'][df_all['School_Type']=='K-8'] = 100*df_all['2010_11_PERF'][df_all['School_Type']=='K-8'].rank()/df_all['2010_11_PERF'][df_all['School_Type']=='K-8'].count()
df_all['2010_11_PERF_PERC'][df_all['School_Type']=='Elementary'] = 100*df_all['2010_11_PERF'][df_all['School_Type']=='Elementary'].rank()/df_all['2010_11_PERF'][df_all['School_Type']=='Elementary'].count()
df_all['2011_12_PERF_PERC'] = Series(np.nan)
df_all['2011_12_PERF_PERC'][df_all['School_Type']=='Middle'] = 100*df_all['2011_12_PERF'][df_all['School_Type']=='Middle'].rank()/df_all['2011_12_PERF'][df_all['School_Type']=='Middle'].count()
df_all['2011_12_PERF_PERC'][df_all['School_Type']=='K-8'] = 100*df_all['2011_12_PERF'][df_all['School_Type']=='K-8'].rank()/df_all['2011_12_PERF'][df_all['School_Type']=='K-8'].count()
df_all['2011_12_PERF_PERC'][df_all['School_Type']=='Elementary'] = 100*df_all['2011_12_PERF'][df_all['School_Type']=='Elementary'].rank()/df_all['2011_12_PERF'][df_all['School_Type']=='Elementary'].count()
df_all['2012_13_PERF_PERC'] = Series(np.nan)
df_all['2012_13_PERF_PERC'][df_all['School_Type']=='Middle'] = 100*df_all['2012_13_PERF'][df_all['School_Type']=='Middle'].rank()/df_all['2012_13_PERF'][df_all['School_Type']=='Middle'].count()
df_all['2012_13_PERF_PERC'][df_all['School_Type']=='K-8'] = 100*df_all['2012_13_PERF'][df_all['School_Type']=='K-8'].rank()/df_all['2012_13_PERF'][df_all['School_Type']=='K-8'].count()
df_all['2012_13_PERF_PERC'][df_all['School_Type']=='Elementary'] = 100*df_all['2012_13_PERF'][df_all['School_Type']=='Elementary'].rank()/df_all['2012_13_PERF'][df_all['School_Type']=='Elementary'].count()



X_all = df_all[['2006_07_SCORE','2007_08_SCORE','2008_09_SCORE','2009_10_SCORE','2010_11_SCORE','2011_12_SCORE','2012_13_SCORE']]
medians = X_all.median()

X_imputed = X_all.copy()
for index,row in X_imputed.iterrows():
    if row[:7].isnull().sum()==7:
        X_imputed.iloc[index,0:7] = medians[:7]
    elif row[:7].isnull().sum()>0:
        ind = row[:7][row[:7].isnull() == True].index.tolist()
        X_imputed[index:index+1][ind] = row[:7].median()


model = linear_model.LinearRegression()

X_train = X_imputed[['2006_07_SCORE','2007_08_SCORE','2008_09_SCORE','2009_10_SCORE','2010_11_SCORE']]
y_train = X_imputed['2011_12_SCORE']

model.fit(X_train,y_train)
out = model.predict(X_train)

#df_all = df_scores
df_all['2011_12_SCORE_PRED'] = DataFrame(out)

RMSE_auto_train = ((df_all['2011_12_SCORE_PRED']-df_all['2011_12_SCORE'])**2).mean()**(0.5)
print "RMSE of autoregression training data: " +  str(RMSE_auto_train)

X_test = X_imputed[['2007_08_SCORE','2008_09_SCORE','2009_10_SCORE','2010_11_SCORE','2011_12_SCORE']]
y_test = X_imputed['2012_13_SCORE']

out = model.predict(X_test)
df_all['2012_13_SCORE_PRED'] = DataFrame(out)

RMSE_auto_test = ((df_all['2012_13_SCORE_PRED']-df_all['2012_13_SCORE'])**2).mean()**(0.5)
print "RMSE of autoregression on test data: " +  str(RMSE_auto_test)

coef = model.coef_
print "coefficients of autoregression: " + str(coef)

inter = model.intercept_
print "intercept of autoregression: " + str(inter)

d = {'Middle':Series([29.1, 37.3, 53.0, 67.7]),'K-8':Series([32.0, 40.6, 53.2, 63.1]),'Elementary':Series([30.0, 36.5, 48.8, 60.1])}
cut = DataFrame(d)

df_all['2012_13_GRADE_PRED'] = Series(np.nan)

df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] < cut['Middle'][0]) & (df_all['School_Type'] == 'Middle')] = 'F'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['Middle'][0]) & (df_all['2012_13_SCORE_PRED'] < cut['Middle'][1]) & (df_all['School_Type'] == 'Middle')] = 'D'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['Middle'][1]) & (df_all['2012_13_SCORE_PRED'] < cut['Middle'][2]) & (df_all['School_Type'] == 'Middle')] = 'C'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['Middle'][2]) & (df_all['2012_13_SCORE_PRED'] < cut['Middle'][3]) & (df_all['School_Type'] == 'Middle')] = 'B'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['Middle'][3]) & (df_all['School_Type'] == 'Middle')] = 'A'


df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] < cut['K-8'][0]) & (df_all['School_Type'] == 'K-8')] = 'F'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['K-8'][0]) & (df_all['2012_13_SCORE_PRED'] < cut['K-8'][1]) & (df_all['School_Type'] == 'K-8')] = 'D'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['K-8'][1]) & (df_all['2012_13_SCORE_PRED'] < cut['K-8'][2]) & (df_all['School_Type'] == 'K-8')] = 'C'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['K-8'][2]) & (df_all['2012_13_SCORE_PRED'] < cut['K-8'][3]) & (df_all['School_Type'] == 'K-8')] = 'B'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['K-8'][3]) & (df_all['School_Type'] == 'K-8')] = 'A'

df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] < cut['Elementary'][0]) & (df_all['School_Type'] == 'Elementary')] = 'F'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['Elementary'][0]) & (df_all['2012_13_SCORE_PRED'] < cut['Elementary'][1]) & (df_all['School_Type'] == 'Elementary')] = 'D'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['Elementary'][1]) & (df_all['2012_13_SCORE_PRED'] < cut['Elementary'][2]) & (df_all['School_Type'] == 'Elementary')] = 'C'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['Elementary'][2]) & (df_all['2012_13_SCORE_PRED'] < cut['Elementary'][3]) & (df_all['School_Type'] == 'Elementary')] = 'B'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['Elementary'][3]) & (df_all['School_Type'] == 'Elementary')] = 'A'

conv_dict={'A':5.,'B':4.,'C':3.,'D':2.,'F':1,'None':np.nan}
df_all.head()
df_grade = df_all[['DBN','School','School_Type']]
df_grade['2012_13_GRADE'] = df_all['2012_13_GRADE'].apply(conv_dict.get)
df_grade['2012_13_GRADE_PRED'] = df_all['2012_13_GRADE_PRED'].apply(conv_dict.get)


RMSE_grade = ((df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED'])**2).mean()**(0.5)
print RMSE_grade

print 'percentage of grades correct on test data: ' + str(sum(abs(df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 0)/float(df_all['2012_13_GRADE'].count()))
print 'percentage of grades 1 off on test data: ' + str(sum(abs(df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 1)/float(df_all['2012_13_GRADE'].count()))
print 'percentage of grades 2 off on test data: ' + str(sum(abs(df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 2)/float(df_all['2012_13_GRADE'].count()))
print 'percentage of grades 3 off on test data: ' + str(sum(abs(df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 3)/float(df_all['2012_13_GRADE'].count()))
print 'percentage of grades 4 off on test data: ' + str(sum(abs(df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 4)/float(df_all['2012_13_GRADE'].count()))


model.fit(X_test,y_test)
out = model.predict(X_test)

df_all['2012_13_SCORE_PRED'] = DataFrame(out)

RMSE_auto_final = ((df_all['2012_13_SCORE_PRED']-df_all['2012_13_SCORE'])**2).mean()**(0.5)
print "RMSE of autoregression final data: " +  str(RMSE_auto_final)

df_all['2012_13_GRADE_PRED'] = Series(np.nan)

df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] < cut['Middle'][0]) & (df_all['School_Type'] == 'Middle')] = 'F'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['Middle'][0]) & (df_all['2012_13_SCORE_PRED'] < cut['Middle'][1]) & (df_all['School_Type'] == 'Middle')] = 'D'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['Middle'][1]) & (df_all['2012_13_SCORE_PRED'] < cut['Middle'][2]) & (df_all['School_Type'] == 'Middle')] = 'C'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['Middle'][2]) & (df_all['2012_13_SCORE_PRED'] < cut['Middle'][3]) & (df_all['School_Type'] == 'Middle')] = 'B'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['Middle'][3]) & (df_all['School_Type'] == 'Middle')] = 'A'


df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] < cut['K-8'][0]) & (df_all['School_Type'] == 'K-8')] = 'F'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['K-8'][0]) & (df_all['2012_13_SCORE_PRED'] < cut['K-8'][1]) & (df_all['School_Type'] == 'K-8')] = 'D'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['K-8'][1]) & (df_all['2012_13_SCORE_PRED'] < cut['K-8'][2]) & (df_all['School_Type'] == 'K-8')] = 'C'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['K-8'][2]) & (df_all['2012_13_SCORE_PRED'] < cut['K-8'][3]) & (df_all['School_Type'] == 'K-8')] = 'B'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['K-8'][3]) & (df_all['School_Type'] == 'K-8')] = 'A'

df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] < cut['Elementary'][0]) & (df_all['School_Type'] == 'Elementary')] = 'F'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['Elementary'][0]) & (df_all['2012_13_SCORE_PRED'] < cut['Elementary'][1]) & (df_all['School_Type'] == 'Elementary')] = 'D'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['Elementary'][1]) & (df_all['2012_13_SCORE_PRED'] < cut['Elementary'][2]) & (df_all['School_Type'] == 'Elementary')] = 'C'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['Elementary'][2]) & (df_all['2012_13_SCORE_PRED'] < cut['Elementary'][3]) & (df_all['School_Type'] == 'Elementary')] = 'B'
df_all['2012_13_GRADE_PRED'][(df_all['2012_13_SCORE_PRED'] >= cut['Elementary'][3]) & (df_all['School_Type'] == 'Elementary')] = 'A'

conv_dict={'A':5.,'B':4.,'C':3.,'D':2.,'F':1,'None':np.nan}
df_all.head()
df_grade = df_all[['DBN','School','School_Type']]
df_grade['2012_13_GRADE'] = df_all['2012_13_GRADE'].apply(conv_dict.get)
df_grade['2012_13_GRADE_PRED'] = df_all['2012_13_GRADE_PRED'].apply(conv_dict.get)


RMSE_grade = ((df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED'])**2).mean()**(0.5)
print RMSE_grade

print 'percentage of grades correct on re-training data: ' + str(sum(abs(df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 0)/float(df_all['2012_13_GRADE'].count()))
print 'percentage of grades 1 off on re-training data: ' + str(sum(abs(df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 1)/float(df_all['2012_13_GRADE'].count()))
print 'percentage of grades 2 off on re-training data: ' + str(sum(abs(df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 2)/float(df_all['2012_13_GRADE'].count()))
print 'percentage of grades 3 off on re-training data: ' + str(sum(abs(df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 3)/float(df_all['2012_13_GRADE'].count()))
print 'percentage of grades 4 off on re-training data: ' + str(sum(abs(df_grade['2012_13_GRADE']-df_grade['2012_13_GRADE_PRED']) == 4)/float(df_all['2012_13_GRADE'].count()))


X_final = X_imputed[['2008_09_SCORE','2009_10_SCORE','2010_11_SCORE','2011_12_SCORE','2012_13_SCORE']]

out = model.predict(X_final)
df_all['2013_14_SCORE_PRED'] = DataFrame(out)

coef = model.coef_
print "coefficients of autoregression: " + str(coef)

inter = model.intercept_
print "intercept of autoregression: " + str(inter)

df_all['2013_14_GRADE_PRED'] = Series(np.nan)

df_all['2013_14_GRADE_PRED'][(df_all['2013_14_SCORE_PRED'] < cut['Middle'][0]) & (df_all['School_Type'] == 'Middle')] = 'F'
df_all['2013_14_GRADE_PRED'][(df_all['2013_14_SCORE_PRED'] >= cut['Middle'][0]) & (df_all['2013_14_SCORE_PRED'] < cut['Middle'][1]) & (df_all['School_Type'] == 'Middle')] = 'D'
df_all['2013_14_GRADE_PRED'][(df_all['2013_14_SCORE_PRED'] >= cut['Middle'][1]) & (df_all['2013_14_SCORE_PRED'] < cut['Middle'][2]) & (df_all['School_Type'] == 'Middle')] = 'C'
df_all['2013_14_GRADE_PRED'][(df_all['2013_14_SCORE_PRED'] >= cut['Middle'][2]) & (df_all['2013_14_SCORE_PRED'] < cut['Middle'][3]) & (df_all['School_Type'] == 'Middle')] = 'B'
df_all['2013_14_GRADE_PRED'][(df_all['2013_14_SCORE_PRED'] >= cut['Middle'][3]) & (df_all['School_Type'] == 'Middle')] = 'A'

df_all['2013_14_GRADE_PRED'][(df_all['2013_14_SCORE_PRED'] < cut['K-8'][0]) & (df_all['School_Type'] == 'K-8')] = 'F'
df_all['2013_14_GRADE_PRED'][(df_all['2013_14_SCORE_PRED'] >= cut['K-8'][0]) & (df_all['2013_14_SCORE_PRED'] < cut['K-8'][1]) & (df_all['School_Type'] == 'K-8')] = 'D'
df_all['2013_14_GRADE_PRED'][(df_all['2013_14_SCORE_PRED'] >= cut['K-8'][1]) & (df_all['2013_14_SCORE_PRED'] < cut['K-8'][2]) & (df_all['School_Type'] == 'K-8')] = 'C'
df_all['2013_14_GRADE_PRED'][(df_all['2013_14_SCORE_PRED'] >= cut['K-8'][2]) & (df_all['2013_14_SCORE_PRED'] < cut['K-8'][3]) & (df_all['School_Type'] == 'K-8')] = 'B'
df_all['2013_14_GRADE_PRED'][(df_all['2013_14_SCORE_PRED'] >= cut['K-8'][3]) & (df_all['School_Type'] == 'K-8')] = 'A'

df_all['2013_14_GRADE_PRED'][(df_all['2013_14_SCORE_PRED'] < cut['Elementary'][0]) & (df_all['School_Type'] == 'Elementary')] = 'F'
df_all['2013_14_GRADE_PRED'][(df_all['2013_14_SCORE_PRED'] >= cut['Elementary'][0]) & (df_all['2013_14_SCORE_PRED'] < cut['Elementary'][1]) & (df_all['School_Type'] == 'Elementary')] = 'D'
df_all['2013_14_GRADE_PRED'][(df_all['2013_14_SCORE_PRED'] >= cut['Elementary'][1]) & (df_all['2013_14_SCORE_PRED'] < cut['Elementary'][2]) & (df_all['School_Type'] == 'Elementary')] = 'C'
df_all['2013_14_GRADE_PRED'][(df_all['2013_14_SCORE_PRED'] >= cut['Elementary'][2]) & (df_all['2013_14_SCORE_PRED'] < cut['Elementary'][3]) & (df_all['School_Type'] == 'Elementary')] = 'B'
df_all['2013_14_GRADE_PRED'][(df_all['2013_14_SCORE_PRED'] >= cut['Elementary'][3]) & (df_all['School_Type'] == 'Elementary')] = 'A'

df_final = df_all[['DBN','School','School_Type','2013_14_SCORE_PRED','2013_14_GRADE_PRED',\
'2012_13_SCORE','2012_13_GRADE','2011_12_SCORE','2011_12_GRADE','2010_11_SCORE','2010_11_GRADE','2009_10_SCORE','2009_10_GRADE','2008_09_SCORE','2008_09_GRADE','2007_08_SCORE','2007_08_GRADE','2006_07_SCORE','2006_07_GRADE',\
'2012_13_PERF_PERC','2011_12_PERF_PERC','2010_11_PERF_PERC','2009_10_PERF_PERC','2008_09_PERF_PERC','2007_08_PERF_PERC','2006_07_PERF_PERC']]

df_final.to_csv('./data/dump_final.csv',float_format ='%.0f')