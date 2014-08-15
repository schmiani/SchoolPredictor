#Autoregression predicting score of Elementary, K-8 and Middle Schools

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


df_mysql = psql.read_sql('SELECT * FROM allyears_ems', con=mydb)


df_mysql.head()


model = linear_model.LinearRegression()


X = df_mysql[['2006_07_SCORE','2007_08_SCORE','2008_09_SCORE','2009_10_SCORE','2010_11_SCORE']]


imputer = preprocessing.Imputer(strategy='median')
imputer.fit(X)
X_imputed = imputer.transform(X)


y = df_mysql['2011_12_SCORE']
imputer = preprocessing.Imputer(strategy='median',axis = 1)
imputer.fit(y)
y_imputed = imputer.transform(y)


model.fit(X_imputed,np.ravel(y_imputed))


out = model.predict(X_imputed)


model.score(X_imputed,np.ravel(y_imputed))


df = df_mysql
df['auto_pred_2012'] = DataFrame(out)


RMSE_auto_train = ((df['auto_pred_2012']-df['2011_12_SCORE'])**2).mean()**(0.5)
print "RMSE of autoregression on training data: " +  str(RMSE_auto_train)

X_test = df_mysql[['2007_08_SCORE','2008_09_SCORE','2009_10_SCORE','2010_11_SCORE','2011_12_SCORE']]

imputer = preprocessing.Imputer(strategy='median')
imputer.fit(X_test)
X_test_imputed = imputer.transform(X_test)

y_test = df_mysql['2012_13_SCORE']
imputer = preprocessing.Imputer(strategy='median',axis = 1)
imputer.fit(y_test)
y_test_imputed = imputer.transform(y_test)

out = model.predict(X_test_imputed)

df['auto_pred_2013'] = DataFrame(out)

RMSE_auto_test = ((df['auto_pred_2013']-df['2012_13_SCORE'])**2).mean()**(0.5)
print "RMSE of autoregression on test data: " +  str(RMSE_auto_test)

coef = model.coef_
print "coefficients of autoregression: " + str(coef)

inter = model.intercept_
print "intercept of autoregression: " + str(inter)




