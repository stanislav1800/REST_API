# REST API для туристических горных перевалов.

## Описание задачи:

ФСТР заказала студентам SkillFactory разработать мобильное приложение для Android и IOS, которое упростило бы туристам задачу по отправке данных о перевале и сократило время обработки запроса до трёх дней.

Пользоваться мобильным приложением будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР, как только появится доступ в Интернет.

Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

Пользователь с помощью мобильного приложения будет передавать в ФСТР следующие данные о перевале:

- координаты перевала и его высота;
- имя пользователя;
- почта и телефон пользователя;
- название перевала;
- несколько фотографий перевала.

## Реализованы методы:

### Метод POST submitData
Когда турист поднимется на перевал, он сфотографирует его и внесёт нужную информацию с помощью мобильного приложения:

- координаты объекта и его высоту;
- название объекта;
- несколько фотографий;
- информацию о пользователе, который передал данные о перевале:
- имя пользователя (ФИО строкой);
- почта;
- телефон.

Метод submitData принимает JSON в теле запроса с информацией о перевале. Ниже находится пример такого JSON-а:

```
{
	"beauty_title": "пер.",
	"title": "Пхия",
	"other_titles": "Триев",
	"connect": "new",
	"add_time": "2024-05-08T12:35:05.229625Z",
	"user": {
		"email": "qwerty@mail.ru",
		"fam": "Пупкин",
		"name": "Василий",
		"otc": "Иванович",
		"phone_nombers": "+7 555 55 55"
	},
	"coords": {
		"latitude": 45.3842,
		"longitude": 7.1525,
		"height": 1200
	},
	"level": {
		"winter": "2A",
		"summer": "1А",
		"autumn": "1А",
		"spring": "2A"
	},
	"images": []
}
```
Результат метода: JSON

status — код HTTP, целое число:
500 — ошибка при выполнении операции;
400 — Bad Request (при нехватке полей);
200 — успех.
message — строка.

Примеры:

```
{ "status": 500, "message": "Ошибка подключения к базе данных","id": null}
{ "status": 200, "message": null, "id": 42 }
```

### Метод GET /submitData/<id> 
Получает одну запись (перевал) по её id.
Выводит всю информацию об объекте, в том числе статус модерации.

```
{
	"id": 4,
	"beauty_title": "пер.",
	"title": "Пхия2",
	"other_titles": "Триев2",
	"connect": "new",
	"add_time": "2024-05-08T12:35:05.229625Z",
	"user": {
		"email": "qwerty@mail.ru",
		"fam": "Пупкин",
		"name": "Василий",
		"otc": "Иванович",
		"phone_nombers": "+7 555 55 55"
	},
	"coords": {
		"latitude": 45.3842,
		"longitude": 7.1525,
		"height": 1200
	},
	"level": {
		"winter": "2A",
		"summer": "1А",
		"autumn": "1А",
		"spring": "2A"
	},
	"images": [],
	"status": "pending"
}
```

### Метод PATCH /submitData/<id>
Редактирует существующую запись, если она в статусе new.
Редактировать можно все поля, кроме тех, что содержат в себе ФИО, адрес почты и номер телефона. Метод принимает тот же самый json, который принимал метод POST submitData.

В качестве результата верни два значения:
state:
1 — если успешно удалось отредактировать запись в базе данных.
0 — в противном случае.

```
{
	"state": "0",
	"message": "отклонено. причина: на рассмотрении"
}
```

### Метод GET /submitData/?user__email=<email> 
Выводит список данных обо всех объектах, которые пользователь с почтой <email> отправил на сервер.
```
{
	"count": 20,
	"next": "http://127.0.0.1:8000/api/pereval/?limit=10&offset=10&user__email=qwerty%40mail.ru",
	"previous": null,
	"results": [
		{
			"id": 1,
			"beauty_title": "пер.",
			"title": "Пхия",
			"other_titles": "Триев",
			"connect": "new",
			"add_time": "2024-05-08T12:30:44.633982Z",
			"user": {
				"email": "qwerty@mail.ru",
				"fam": "Пупкин",
				"name": "Василий",
				"otc": "Иванович",
				"phone_nombers": "+7 555 55 55"
			},
			"coords": {
				"latitude": 45.3842,
				"longitude": 7.1525,
				"height": 1200
			},
			"level": {
				"winter": "2A",
				"summer": "1А",
				"autumn": "1А",
				"spring": "2A"
			},
			"images": [
				{
					"data": "http://127.0.0.0/image.jpg",
					"title": "Седловина"
				},
				{
					"data": "http://127.0.0.0/image.jpg",
					"title": "Седловина"
				}
				]
		}
		]
}
```

