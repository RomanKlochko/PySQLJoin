# Сделать выборку студентов по названию университета из внешних Json файлов: students и universities.
# Json файлы оформлены в виде списка.
import time

start = time.clock()

import json

with open('/home/roman/projects/MyPRJ/PySQL/PySQLJoin/Json_Load_Join/Json_univs.json') as data_file:
    data = json.load(data_file)

filter = input()
where_city = []
where_student = []
where_city = [item["id"] for item in data["universities"] if item["name"] == filter]

with open('/home/roman/projects/MyPRJ/PySQL/PySQLJoin/Json_Load_Join/Json_students.json') as data_file:
    data = json.load(data_file)

where_student = [item for item in data["students"] if item["univ_id"] == where_city[0]]

from pprint import pprint
pprint(where_student)

end = time.clock()
print(start)
print(end)
print (end - start)