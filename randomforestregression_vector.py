#Random Forest Regression (features like in vector autoregression)
#not better than simple vector autoregression

import MySQLdb
import pandas.io.sql as psql
from pandas import *
import numpy as np
import scipy.stats
import scipy
from sklearn import ensemble
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


model = ensemble.RandomForestRegressor(max_depth=3,max_features=3,n_estimators=1000,min_samples_leaf=1)


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

#model.score(X_imputed,np.ravel(y_imputed))

df = df_scores
df['rfreg_pred_2012'] = DataFrame(out)

RMSE_rfreg_train = ((df['rfreg_pred_2012']-df['2011_12_SCORE'])**2).mean()**(0.5)
print "RMSE of random forest regression on training data: " +  str(RMSE_rfreg_train)

X_test = df_all[['2007_08_SCORE','2008_09_SCORE','2009_10_SCORE','2010_11_SCORE','2011_12_SCORE','2007_08_PERF','2008_09_PERF','2009_10_PERF','2010_11_PERF','2011_12_PERF']]

imputer = preprocessing.Imputer(strategy='median')
imputer.fit(X_test)
X_test_imputed = imputer.transform(X_test)

y_test = df_all['2012_13_SCORE']
imputer = preprocessing.Imputer(strategy='median',axis = 1)
imputer.fit(y_test)
y_test_imputed = imputer.transform(y_test)

out = model.predict(X_test_imputed)

df['rfreg_pred_2013'] = DataFrame(out)

RMSE_rfreg_test = ((df['rfreg_pred_2013']-df['2012_13_SCORE'])**2).mean()**(0.5)
print "RMSE of random forest regression on test data: " +  str(RMSE_rfreg_test)

inter = model.feature_importances_
print "feature importance: " + str(inter)

