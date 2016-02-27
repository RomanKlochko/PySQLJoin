# Сделать выборку студентов по названию университета из внешних Json файлов: students и universities.

import time

start = time.clock()

import json

with open('/home/roman/projects/MyPRJ/PySQL/PySQLJoin/Json_Load_Join/Json_univs.json') as data_file:
    data = json.load(data_file)

filter_univ_city = input()
filter_univ_id = 0

for i in data["universities"]:
	if i["name"] == filter_univ_city:
		filter_univ_id = i["id"]

with open('/home/roman/projects/MyPRJ/PySQL/PySQLJoin/Json_Load_Join/Json_students.json') as data_file:
    data = json.load(data_file)

for i in data["students"]:
	if i["univ_id"] == filter_univ_id:
		print(i)

end = time.clock()
print(start)
print(end)
print (end - start)