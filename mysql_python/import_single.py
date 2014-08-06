import csv
import MySQLdb
import numpy as np
import sys
import re

def get_header(info):
    flag = False
    while flag == False:
        header = info.next()
        if header[1] == 'DBN':
            flag = True
    return header

def import_file(input_file):
    mydb = MySQLdb.connect(host='localhost',
        user='root',
        passwd='password',
        db='school')
    cur = mydb.cursor()

    match = re.match(r".*data/\d+_(\d+)/*",input_file)
    year = match.group(1)

    # drop table and create them new
    table_name = 'All_%s'
    table_name = table_name % year
    query = 'DROP TABLE IF EXISTS ' + table_name
    cur.execute(query)

    # read in basic data and put into mysql table
    # get size of table
    info = csv.reader(file(input_file))

    header = get_header(info)

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
    header = get_header(info)

    for i,row in enumerate(info):
        for ind in indexes_sort:
            del row[ind]
        for j,cell in enumerate(row):
            L[i,j] = len(cell)

    maxwidth = L.max(0)

    # read in data and put into table
    info = csv.reader(file(input_file))
    header = get_header(info)

    headersql = [s.replace('-','_').replace(' ','_').replace('\n','_').replace('*','').replace('/','_') for s in header]

    for i in range(count):
        headersql.remove('')

    querylist = []

    for i in range(ncols):
        querylist.append(headersql[i] + ' VARCHAR(' + str(int(maxwidth[i])) + ')')

    query = 'CREATE TABLE ' + table_name + '(' + ",".join(querylist) + ')'
    cur.execute(query)

    query = 'INSERT INTO ' + table_name + '(' + '%s, ' *(len(headersql)-1) + '%s)'
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


def main():
    fname = sys.argv[1]
    import_file(fname)
    
if __name__ == '__main__':
    main()