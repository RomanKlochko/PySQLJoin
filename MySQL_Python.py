# Подключиться к базе данных QALIGHT через MySQL Server. Сделать выборку студентов по названию университета.

import time

start = time.clock()
import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='123', db='qalight', charset='utf8')
cur = conn.cursor()
cur.execute("select * from students join universities on students.univ_id=universities.id where universities.name = 'ХАИ'")
# print cur.description
# r = cur.fetchall()
# print r
# ...or...
for r in cur:
   print (r)
cur.close()
conn.close()
end = time.clock()
print(start)
print(end)
print (end - start)