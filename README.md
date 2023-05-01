# api_final

## О проекте

Проект позволяет делать запросы к социальной сети Yatube через API.
С помощью него можно:
- публиквать записи
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

## Автор:
 :grinning: Lenar :sunglasses::boom: