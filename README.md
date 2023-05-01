# api_final

## О проекте

Проект позволяет делать запросы к социальной сети Yatube через API.
С помощью него можно:
- публикoвать записи
- комментировать записи
- подписываться на других авторов

## Стек технологий

- Python
- Django
- DFR
- JWT
- Djoser

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/LenarFazlyev/api_final_yatube.git
```

```
cd api_final_yatube.git
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Script/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Документация в формате Redoc:
[Redoc](yatube_api/static/redoc.yaml)

## Примеры запросов:
Для большенства запросов пользователь должен быть авторизован, а также необходимо получить токен.
Для получения токена необходимо выполнить запрос: http://127.0.0.1:8000/api/v1/jwt/create/
параметры: POST запрос
{
   "username": "username",
   "password": "password"
}

...api/v1/posts/
    * GET - запрос всех постов
    * POST - создать пост.

другие примеры можно посмотреть в [Redoc](yatube_api/static/redoc.yaml)


## Автор:
 :grinning: Lenar :sunglasses::boom: