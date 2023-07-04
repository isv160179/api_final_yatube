## Описание:

Проект YATUBE_API - является финальным домашним заданием по теме 
курса Яндекс.Практикум "API: интерфейс взаимодействия программ."
Проект написан с использованием DjangoRestFramework.
Для идентификации и аутентификации пользователей использованы JWT-токены.
Данный проект позволяет осуществлять взаимодействие с помощью эндпоинтов API 
с базой данных, где хранится информация о постах пользователей, комментариях 
к этим постам и сообществах. Так же есть возможность оформить подписку на 
понравившегося автора поста.
Формат обмена данными - JavaScript Object Notation (JSON)


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/isv160179/api_final_yatube.git
```

```
cd kittygram
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры использования:

### Работа с постами:

Получить список всех публикаций:

GET запрос на эндпоинт
```
http://127.0.0.1:8000/api/v1/posts/
```
Для постраничной выдачи применяйте параметры limit и offset.


Добавление новой публикации в коллекцию публикаций:

POST запрос на эндпоинт
```
http://127.0.0.1:8000/api/v1/posts/
```
В теле запроса в виде JSON-строки необходимо указать следующие параметры:
"text": "Ваш текст публикации" *(обязательное поле)*,
"image": "Рисунок в кодировке base64" *(необязательное поле)*,
"group": номер сообщества *(необязательное поле)*.


Для получения информации по конкретному посту:

GET запрос на эндпоинт
```
http://127.0.0.1:8000/api/v1/posts/{id_поста}/
```

### Работа с комментариями к постам:

Запросы нужно отправлять на эндпоинты: 
```
http://127.0.0.1:8000/api/v1/posts/{id_поста}/comments/
```
```
http://127.0.0.1:8000/api/v1/posts/{id_поста}/comments/{id_комментария}/
```