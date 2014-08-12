#Autoregression predicting score of Elementary, K-8 and Middle Schools

# In[1]:

import MySQLdb
import pandas.io.sql as psql
from pandas import *
import numpy as np
import scipy.stats
import scipy
from sklearn import linear_model
from sklearn import preprocessing


# In[2]:

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='password',
    db='school')


# In[3]:

df_mysql = psql.read_sql('SELECT * FROM allyears_ems', con=mydb)


# In[4]:

df_mysql.head()


# In[5]:

model = linear_model.LinearRegression()
model


# In[6]:

X = df_mysql[['2006_07_SCORE','2007_08_SCORE','2008_09_SCORE','2009_10_SCORE','2010_11_SCORE']]


# In[7]:

imputer = preprocessing.Imputer(strategy='median')
imputer.fit(X)
X_imputed = imputer.transform(X)


# In[8]:

y = df_mysql['2011_12_SCORE']
imputer = preprocessing.Imputer(strategy='median',axis = 1)
imputer.fit(y)
y_imputed = imputer.transform(y)


# In[9]:

model.fit(X_imputed,transpose(y_imputed))


# In[10]:

out = model.predict(X_imputed)


# In[11]:

model.score(X_imputed,transpose(y_imputed))


# In[12]:

df = df_mysql
df['auto_pred_2012'] = DataFrame(out)


# In[13]:

df.head()


# In[19]:

RMSE_auto_train = ((df['auto_pred_2012']-df['2011_12_SCORE'])**2).mean()**(0.5)
print "RMSE of autoregression training data: " +  str(RMSE_auto_train)


# In[20]:

X_test = df_mysql[['2007_08_SCORE','2008_09_SCORE','2009_10_SCORE','2010_11_SCORE','2011_12_SCORE']]


# In[21]:

imputer = preprocessing.Imputer(strategy='median')
imputer.fit(X_test)
X_test_imputed = imputer.transform(X_test)


# In[22]:

y_test = df_mysql['2012_13_SCORE']
imputer = preprocessing.Imputer(strategy='median',axis = 1)
imputer.fit(y_test)
y_test_imputed = imputer.transform(y_test)


# In[23]:

out = model.predict(X_test_imputed)


# In[24]:

df['auto_pred_2013'] = DataFrame(out)


# In[25]:

df.head()


# In[26]:

RMSE_auto_test = ((df['auto_pred_2013']-df['2012_13_SCORE'])**2).mean()**(0.5)
print "RMSE of autoregression on test data: " +  str(RMSE_auto_test)


# In[27]:

coef = model.coef_
print "coefficients of autoregression: " + str(coef)


# In[28]:

inter = model.intercept_
print "intercept of autoregression: " + str(inter)




