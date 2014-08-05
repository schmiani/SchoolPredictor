import csv
import MySQLdb
import numpy as np
import time

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='password',
    db='school')
cur = mydb.cursor()
# drop tables and create them new
cur.execute('DROP TABLE IF EXISTS All_2013')

input_file = '../data/2012_2013_All_ProgressReport_Results_2013_12_19.csv'

# read in basic data and put into mysql table
# get size of table
info = csv.reader(file(input_file))
flag = False
while flag == False:
    header = info.next()
    if header[1] == 'DBN':
        flag = True

count = 0
indexes = []
for i,s in enumerate(header):
    if s == '':
        count += 1
        indexes.append(i)
nrows = 0
for row in info:
    nrows = nrows+1
indexes_sort = sorted(indexes, reverse=True)
for ind in indexes_sort:
    del row[ind]
ncols = len(row)
L = np.zeros((nrows,ncols))

# get maximum width of columns in table
info = csv.reader(file(input_file))
flag = False
while flag == False:
    header = info.next()
    if header[1] == 'DBN':
        flag = True

for i,row in enumerate(info):
    for ind in indexes_sort:
        del row[ind]
    for j,cell in enumerate(row):
        L[i,j] = len(cell)

maxwidth = L.max(0)

# read in data and put into table
info = csv.reader(file(input_file))
flag = False
while flag == False:
    header = info.next()
    if header[1] == 'DBN':
        flag = True
        
headersql = [s.replace('-','_').replace(' ','_').replace('\n','_').replace('*','') for s in header]

for i in range(count):
    headersql.remove('')

querylist = []

for i in range(ncols):
    querylist.append(headersql[i] + ' VARCHAR(' + str(int(maxwidth[i])) + ')')

query = 'CREATE TABLE All_2013(' + ",".join(querylist) + ')'
cur.execute(query)

query = 'INSERT INTO All_2013(' + '%s, ' *(len(headersql)-1) + '%s)'
query = query % tuple(headersql)
query = query + ' VALUES(' + '%s, ' *(len(headersql)-1) + '%s)'
for row in info:
    for ind in indexes_sort:
        del row[ind]
    cur.execute(query, row)

mydb.commit()

#close mysql cursor
cur.close()
print "Done"