# Сделать выборку студентов по названию университета из двух таблиц students и universities.
# Json файлы оформлены в виде списка.
import time

start = time.clock()

universities = [
	{
		"id" : 1,
		"name" : "КПИ",
		"rating" : 1257,
		"city" : "Киев"
	},
	{
		"id" : 2,
		"name" : "КНУ",
		"rating" : 608,
		"city" : "Киев"
	},
	{
		"id" : 3,
		"name" : "ЛПУ",
		"rating" : 593,
		"city" : "Львов"
	},
	{
		"id" : 4,
		"name" : "КМА",
		"rating" : 588,
		"city" : "Киев"
	},
	{
		"id" : 5,
		"name" : "ЛГУ",
		"rating" : 556,
		"city" : "Львов"
	},
	{
		"id" : 6,
		"name" : "ХАИ",
		"rating" : 534,
		"city" : "Харьков"
	},
	{
		"id" : 7,
		"name" : "ДПИ",
		"rating" : 529,
		"city" : "Днепропетровск"
	},
	{
		"id" : 8,
		"name" : "ДНТУ",
		"rating" : 501,
		"city" : "Донецк"
	},
	{
		"id" : 9,
		"name" : "ХНАДУ",
		"rating" : 500,
		"city" : "Харьков"
	},
	{
		"id" : 10,
		"name" : "ОНПУ",
		"rating" : 496,
		"city" : "Одесса"
	},
	{
		"id" : 11,
		"name" : "КНУСА",
		"rating" : 483,
		"city" : "Киев"
	},
	{
		"id" : 12,
		"name" : "ТНТУ",
		"rating" : 441,
		"city" : "Тернополь"
	},
	{
		"id" : 13,
		"name" : "ЗДИА",
		"rating" : 427,
		"city" : "Запорожье"
	},
	{
		"id" : 14,
		"name" : "БНАУ",
		"rating" : 399,
		"city" : "Белая Церковь"
	},
	{
		"id" : 15,
		"name" : "ХСХА",
		"rating" : 45,
		"city" : "Херсон"
	}
]

students = [
	{
		"id" : 1,
		"surname" : "Кабанов",
		"name" : "Виталий",
		"gender" : "m",
		"stipend" : 550.00,
		"course" : 4,
		"city" : "Харьков",
		"birthday" : "1990-11-30T22:00Z",
		"univ_id" : 2
	},
	{
		"id" : 2,
		"surname" : "Павленко",
		"name" : "Игорь",
		"gender" : "m",
		"stipend" : 600.00,
		"course" : 1,
		"city" : "Киев",
		"birthday" : "1993-06-20T21:00Z",
		"univ_id" : 5
	},
	{
		"id" : 3,
		"surname" : "Цилюрик",
		"name" : "Тимофей",
		"gender" : "m",
		"stipend" : 600.00,
		"course" : 4,
		"city" : "Херсон",
		"birthday" : "1990-11-04T22:00Z",
		"univ_id" : 3
	},
	{
		"id" : 4,
		"surname" : "Козьменко",
		"name" : "Игнат",
		"gender" : "m",
		"stipend" : 500.00,
		"course" : 1,
		"city" : "Киев",
		"birthday" : "1994-04-25T21:00Z",
		"univ_id" : 6
	},
	{
		"id" : 5,
		"surname" : "Ориненко",
		"name" : "Анатолий",
		"gender" : "m",
		"stipend" : 450.00,
		"course" : 4,
		"city" : "Львов",
		"birthday" : "1990-09-07T21:00Z",
		"univ_id" : 4
	},
	{
		"id" : 6,
		"surname" : "Березовский",
		"name" : "Роман",
		"gender" : "m",
		"stipend" : 750.00,
		"course" : 2,
		"city" : "Киев",
		"birthday" : "1992-03-08T22:00Z",
		"univ_id" : 1
	},
	{
		"id" : 7,
		"surname" : "Пименчук",
		"name" : "Дмитрий",
		"gender" : "m",
		"stipend" : 800.00,
		"course" : 1,
		"city" : "Харьков",
		"birthday" : "1992-11-19T22:00Z",
		"univ_id" : 2
	},
	{
		"id" : 8,
		"surname" : "Шуст",
		"name" : "Марина",
		"gender" : "f",
		"stipend" : 750.00,
		"course" : 1,
		"city" : "Херсон",
		"birthday" : "1993-04-20T21:00Z",
		"univ_id" : 3
	},
	{
		"id" : 9,
		"surname" : "Печальнова",
		"name" : "Алина",
		"gender" : "f",
		"stipend" : 500.00,
		"course" : 2,
		"city" : "Киев",
		"birthday" : "1993-02-24T22:00Z",
		"univ_id" : 6
	},
	{
		"id" : 10,
		"surname" : "Денисенко",
		"name" : "Марк",
		"gender" : "m",
		"stipend" : 500.00,
		"course" : 3,
		"city" : "Киев",
		"birthday" : "1993-06-06T21:00Z",
		"univ_id" : 1
	},
	{
		"id" : 11,
		"surname" : "Корсунская",
		"name" : "Вера",
		"gender" : "f",
		"stipend" : 650.00,
		"course" : 2,
		"city" : "Ровно",
		"birthday" : "1992-07-10T21:00Z",
		"univ_id" : 'null'
	},
	{
		"id" : 12,
		"surname" : "Чайка",
		"name" : "Ольга",
		"gender" : "f",
		"stipend" : 550.00,
		"course" : 5,
		"city" : "Киев",
		"birthday" : "1990-12-29T22:00Z",
		"univ_id" : 5
	},
	{
		"id" : 13,
		"surname" : "Кожушко",
		"name" : "Кристина",
		"gender" : "f",
		"stipend" : 650.00,
		"course" : 3,
		"city" : "Львов",
		"birthday" : "1991-03-17T22:00Z",
		"univ_id" : 4
	},
	{
		"id" : 14,
		"surname" : "Федосеева",
		"name" : "Нина",
		"gender" : "f",
		"stipend" : 750.00,
		"course" : 2,
		"city" : "Днепропетровск",
		"birthday" : "1992-05-21T21:00Z",
		"univ_id" : 7
	},
	{
		"id" : 15,
		"surname" : "Тарара",
		"name" : "Леонид",
		"gender" : "m",
		"stipend" : 900.00,
		"course" : 4,
		"city" : "Киев",
		"birthday" : "1991-05-03T21:00Z",
		"univ_id" : 6
	},
	{
		"id" : 16,
		"surname" : "Земляний",
		"name" : "Данил",
		"gender" : "m",
		"stipend" : 550.00,
		"course" : 5,
		"city" : "Львов",
		"birthday" : "1988-03-05T22:00Z",
		"univ_id" : 4
	},
	{
		"id" : 17,
		"surname" : "Осипуков",
		"name" : "Виталий",
		"gender" : "m",
		"stipend" : 500.00,
		"course" : 1,
		"city" : "Днепропетровск",
		"birthday" : "1993-08-09T21:00Z",
		"univ_id" : 7
	},
	{
		"id" : 18,
		"surname" : "Зевцов",
		"name" : "Андрей",
		"gender" : "m",
		"stipend" : 650.00,
		"course" : 3,
		"city" : "Львов",
		"birthday" : "1991-10-23T22:00Z",
		"univ_id" : 4
	},
	{
		"id" : 19,
		"surname" : "Бородюк",
		"name" : "Никита",
		"gender" : "m",
		"stipend" : 650.00,
		"course" : 2,
		"city" : "Киев",
		"birthday" : "1990-08-29T21:00Z",
		"univ_id" : 6
	},
	{
		"id" : 20,
		"surname" : "Миланивская",
		"name" : "Ольга",
		"gender" : "f",
		"stipend" : 750.00,
		"course" : 5,
		"city" : "Киев",
		"birthday" : "1989-10-21T22:00Z",
		"univ_id" : 5
	},
	{
		"id" : 21,
		"surname" : "Запорожец",
		"name" : "Владимир",
		"gender" : "m",
		"stipend" : 750.00,
		"course" : 5,
		"city" : "Львов",
		"birthday" : 'null',
		"univ_id" : 5
	},
	{
		"id" : 22,
		"surname" : "Саенко",
		"name" : "Сергей",
		"gender" : "m",
		"stipend" : 950.00,
		"course" : 1,
		"city" : "Полтава",
		"birthday" : "1993-04-16T21:00Z",
		"univ_id" : 9
	},
	{
		"id" : 23,
		"surname" : "Коваленко",
		"name" : "Дмитрий",
		"gender" : "m",
		"stipend" : 650.00,
		"course" : 1,
		"city" : "Хмельницкий",
		"birthday" : "1993-07-27T21:00Z",
		"univ_id" : 7
	},
	{
		"id" : 24,
		"surname" : "Маруга",
		"name" : "Ольга",
		"gender" : "f",
		"stipend" : 850.00,
		"course" : 4,
		"city" : "Севастополь",
		"birthday" : "1990-08-02T21:00Z",
		"univ_id" : 4
	},
	{
		"id" : 25,
		"surname" : "Михайловская",
		"name" : "Светлана",
		"gender" : "f",
		"stipend" : 600.00,
		"course" : 2,
		"city" : "Винница",
		"birthday" : "1992-11-17T22:00Z",
		"univ_id" : 13
	},
	{
		"id" : 26,
		"surname" : "Кораблев",
		"name" : "Станислав",
		"gender" : "m",
		"stipend" : 750.00,
		"course" : 2,
		"city" : "Горловка",
		"birthday" : "1992-05-03T21:00Z",
		"univ_id" : 12
	},
	{
		"id" : 27,
		"surname" : "Бородавко",
		"name" : "Михаил",
		"gender" : "m",
		"stipend" : 750.00,
		"course" : 5,
		"city" : "Кременчуг",
		"birthday" : "1989-01-02T22:00Z",
		"univ_id" : 2
	},
	{
		"id" : 28,
		"surname" : "Литвин",
		"name" : "Олег",
		"gender" : "m",
		"stipend" : 450.00,
		"course" : 3,
		"city" : "Ровно",
		"birthday" : "1991-06-09T21:00Z",
		"univ_id" : 14
	},
	{
		"id" : 29,
		"surname" : "Завакевич",
		"name" : "Василий",
		"gender" : "m",
		"stipend" : 800.00,
		"course" : 4,
		"city" : "Мариуполь",
		"birthday" : "1990-11-12T22:00Z",
		"univ_id" : 1
	},
	{
		"id" : 30,
		"surname" : "Забила",
		"name" : "Алексей",
		"gender" : "m",
		"stipend" : 450.00,
		"course" : 3,
		"city" : "Киев",
		"birthday" : "1991-06-20T21:00Z",
		"univ_id" : 13
	},
	{
		"id" : 31,
		"surname" : "Залыева",
		"name" : "Фатима",
		"gender" : "f",
		"stipend" : 650.00,
		"course" : 4,
		"city" : "Горловка",
		"birthday" : "1990-05-17T21:00Z",
		"univ_id" : 3
	},
	{
		"id" : 32,
		"surname" : "Мироненко",
		"name" : "Евгений",
		"gender" : "m",
		"stipend" : 450.00,
		"course" : 2,
		"city" : "Белая Церковь",
		"birthday" : "1992-08-31T21:00Z",
		"univ_id" : 14
	},
	{
		"id" : 33,
		"surname" : "Шелест",
		"name" : "Юрий",
		"gender" : "m",
		"stipend" : 450.00,
		"course" : 2,
		"city" : "Киев",
		"birthday" : "1992-11-07T22:00Z",
		"univ_id" : 4
	},
	{
		"id" : 34,
		"surname" : "Сабатовская",
		"name" : "Ирина",
		"gender" : "f",
		"stipend" : 650.00,
		"course" : 4,
		"city" : "Одесса",
		"birthday" : "1990-02-13T22:00Z",
		"univ_id" : 11
	},
	{
		"id" : 35,
		"surname" : "Ремезов",
		"name" : "Трофим",
		"gender" : "m",
		"stipend" : 600.00,
		"course" : 3,
		"city" : "Киев",
		"birthday" : "1991-07-23T21:00Z",
		"univ_id" : 8
	},
	{
		"id" : 36,
		"surname" : "Винник",
		"name" : "Артур",
		"gender" : "m",
		"stipend" : 500.00,
		"course" : 4,
		"city" : "Ивано-Франковск",
		"birthday" : "1990-03-03T22:00Z",
		"univ_id" : 8
	},
	{
		"id" : 37,
		"surname" : "Запорожец",
		"name" : "Виталий",
		"gender" : "m",
		"stipend" : 350.00,
		"course" : 5,
		"city" : "Луцк",
		"birthday" : "1989-02-27T22:00Z",
		"univ_id" : 13
	},
	{
		"id" : 38,
		"surname" : "Наталич",
		"name" : "Вадим",
		"gender" : "m",
		"stipend" : 600.00,
		"course" : 3,
		"city" : "Макеевка",
		"birthday" : "1991-05-08T21:00Z",
		"univ_id" : 6
	},
	{
		"id" : 39,
		"surname" : "Богацкий",
		"name" : "Дмитрий",
		"gender" : "m",
		"stipend" : 350.00,
		"course" : 5,
		"city" : "Черновцы",
		"birthday" : "1989-10-11T22:00Z",
		"univ_id" : 12
	},
	{
		"id" : 40,
		"surname" : "Кот",
		"name" : "Екатерина",
		"gender" : "f",
		"stipend" : 700.00,
		"course" : 3,
		"city" : "Киев",
		"birthday" : "1991-04-04T21:00Z",
		"univ_id" : 14
	},
	{
		"id" : 41,
		"surname" : "Денисюк",
		"name" : "Данил",
		"gender" : "m",
		"stipend" : 350.00,
		"course" : 4,
		"city" : "Херсон",
		"birthday" : "1990-01-25T22:00Z",
		"univ_id" : 2
	},
	{
		"id" : 42,
		"surname" : "Гладкий",
		"name" : "Денис",
		"gender" : "m",
		"stipend" : 450.00,
		"course" : 4,
		"city" : "Ровно",
		"birthday" : "1990-12-19T22:00Z",
		"univ_id" : 13
	},
	{
		"id" : 43,
		"surname" : "Рубцова",
		"name" : "Евгения",
		"gender" : "f",
		"stipend" : 600.00,
		"course" : 3,
		"city" : "Донецк",
		"birthday" : "1991-10-09T22:00Z",
		"univ_id" : 11
	},
	{
		"id" : 44,
		"surname" : "Гузенко",
		"name" : "Александра",
		"gender" : "f",
		"stipend" : 500.00,
		"course" : 1,
		"city" : "Ровно",
		"birthday" : "1993-11-08T22:00Z",
		"univ_id" : 8
	},
	{
		"id" : 45,
		"surname" : "Рудавский",
		"name" : "Игорь",
		"gender" : "m",
		"stipend" : 500.00,
		"course" : 4,
		"city" : "Винница",
		"birthday" : "1990-10-22T22:00Z",
		"univ_id" : 2
	}
]

filter_univ = input()
filter_univ_id = 0

for i in universities:
	if i["name"] == filter_univ:
		filter_univ_id = i["id"]

for i in students:
	if i["univ_id"] == filter_univ_id:
		print(i)


end = time.clock()
print(start)
print(end)
print (end - start)
