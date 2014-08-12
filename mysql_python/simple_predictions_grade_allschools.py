import MySQLdb
import pandas.io.sql as psql
from pandas import *
import numpy as np
import scipy.stats

#connect to MySQL
mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='password',
    db='school')

#get Multiyear table
df_mysql = psql.read_sql('SELECT * FROM Multiyear', con=mydb)  

#make new DataFrame with relevand columns and convert grades into numbers 
conv_dict={'A':5.,'B':4.,'C':3.,'D':2.,'F':1,'None':np.nan}
df = df_mysql[['BN','SCHOOL_NAME']]
df['2012_2013'] = df_mysql['2012_2013'].apply(conv_dict.get)
df['2011_2012'] = df_mysql['2011_2012'].apply(conv_dict.get)
df['2010_2011'] = df_mysql['2010_11'].apply(conv_dict.get)
df['2009_2010'] = df_mysql['2009_10'].apply(conv_dict.get)
df['2008_2009'] = df_mysql['2008_09'].apply(conv_dict.get)
df['2007_2008'] = df_mysql['2007_08'].apply(conv_dict.get)
df['2006_2007'] = df_mysql['2006_07'].apply(conv_dict.get)

#probablity distribution fro last year (including NaN values)
[hist, bin_edges] = np.histogram(df['2012_2013'],range = (0.5, 5.5),bins = 5)
n = df.shape[0]
ps = hist/float(n)
xs = np.array([1, 2, 3, 4, 5])
nnull = np.array([sum(df['2012_2013'].isnull())/float(n)])
pk = np.concatenate((nnull,ps))
xk = np.concatenate(([0],xs))

#random number generator from probablity distribution for 7th year
tuple = (xk,pk)
custm = scipy.stats.rv_discrete(values=tuple)

#convert 0s back to NaNs
invconv_dict={0:np.nan,1:1,2:2,3:3,4:4,5:5}

#compute RMSE for each iteration
RMSE_rand = np.zeros((100,1))
for i in range(100):
    R = custm.rvs(size=n)
    rand = Series(R).apply(invconv_dict.get)
    RMSE_rand[i,:] = ((rand-df['2012_2013'])**2).mean()**(0.5)

RMSE_rand.mean()
print "Mean RMSE for random from known probability distribution: " + str(RMSE_rand.mean())

#take the known median value 
df['median_pred'] = df['2012_2013'].median()
RMSE_median = ((df['median_pred']-df['2012_2013'])**2).mean()**(0.5)
print "RMSE for using known median value: " + str(RMSE_median)

#take the 6th year to predict 7th year
df['last_pred'] = df['2011_2012']
RMSE_last = ((df['last_pred']-df['2012_2013'])**2).mean()**(0.5)
print "RMSE for using value from previous year: " + str(RMSE_last)

#compute median over all previous years for each shool
df['median_indiv_pred'] = df[['2011_2012','2010_2011','2009_2010','2008_2009','2007_2008','2006_2007']].median(1)
RMSE_median_indiv = ((df['median_indiv_pred']-df['2012_2013'])**2).mean()**(0.5)
print "RMSE for using median over all previous year for each school: " + str(RMSE_median_indiv)