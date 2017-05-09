# -*- coding=utf-8 -*-

import MySQLdb

con = MySQLdb.connect(host='115.28.184.100', port=5001, user='root', passwd='mysql', db='spider')
con.set_character_set('utf8')

cursor = con.cursor()
cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')


sql = 'select pid, address from product_20160805 where address is not null limit 0, 10'
#sql = 'select pid, address from product_20160805 where address is not null'
cursor.execute(sql)

records = cursor.fetchall()

stand = 'update product_20160805 set addr_new = %s where pid = %s'

for pid, record in records:
    record = record.decode('utf-8', 'ignore')
    print  pid, record, type(record)



cursor.close()
con.close()
