### Проект «API для Yatube»
Описание
API для Yatub представляет собой проект социальной сети в которой реализованы следующие возможности, публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.

Автор: Алексей Дегунов

### Технологии
- Python 3.9
- Django
- Django REST Framework
- Django REST Framework SimpleJWT

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ad7595/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать и выполнить миграции:

```
python manage.py makemigrations
python manage.py migrate
```

Создать суперпользователя и снова выполнить миграции:

```
python manage.py createsuperuser
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Документация

Документация доступна по адресу:

```
http://127.0.0.1:8000/redoc
```


### Примеры запросов

Получение публикаций:
>**GET** http://127.0.0.1:8000/api/v1/posts/

Создание публикации:
>**POST** http://127.0.0.1:8000/api/v1/posts/
```
{
  "text": "string",
  ...
}
```

Получение списка групп:
>**GET** http://127.0.0.1:8000/api/v1/groups/

Просмотр комментариев к публикации:
>**GET** http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

Создание комментариев к публикации:
>**POST** http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
{
  "text": "string"
}
```

Посмотреть всех подписчиков пользователя:
>**GET** http://127.0.0.1:8000/api/v1/follow/

Подписаться на автора:
>**POST** http://127.0.0.1:8000/api/v1/follow/
```
{
  "following": "string"(username)
}
```