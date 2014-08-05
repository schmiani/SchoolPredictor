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
cur.execute('DROP TABLE IF EXISTS Multiyear')

# read in basic data and put into mysql table
# get size of table
info = csv.reader(file('../data/20072013_Multiyear_All_ProgressReportGrades_2013_12_19.csv'))
header = info.next()
nrows = 0
for row in info:
    nrows = nrows+1
ncols = len(row)
L = np.zeros((nrows,ncols))

# get maximum width of columns in table
info = csv.reader(file('../data/20072013_Multiyear_All_ProgressReportGrades_2013_12_19.csv'))
header = info.next()
for i,row in enumerate(info):
    for j,cell in enumerate(row):
        L[i,j] = len(cell)

maxwidth = L.max(0)

# read in data and put into table
info = csv.reader(file('../data/20072013_Multiyear_All_ProgressReportGrades_2013_12_19.csv'))
header = info.next()
headersql = [s.replace('-','_').replace(' PROGRESS REPORT GRADE','').replace(' PROGRESS\nREPORT GRADE','').replace(' ','_') for s in header]

querylist = []

for i in range(ncols):
    querylist.append(headersql[i] + ' VARCHAR(' + str(int(maxwidth[i])) + ')')

query = 'CREATE TABLE Multiyear(' + ",".join(querylist) + ')'
cur.execute(query)

query = 'INSERT INTO Multiyear(' + '%s, ' *(len(header)-1) + '%s)'
query = query % tuple(headersql)
query = query + ' VALUES(' + '%s, ' *(len(header)-1) + '%s)'
for row in info:
    cur.execute(query, row)

mydb.commit()

#close mysql cursor
cur.close()
print "Done"