# YAMDB
## Описание
Данный проект позволяет пользователям оставлять отзывы на любимую музыку, песни, фильмы и книги и всё, что угодно.
Пользователи могут следить за любимыми обозревателями, писать комментарии, вступать в группы и, конечно же, оставлять свои отзывы и получать фидбэк.
Что не мало важно, пользователям также можно ставить оценки произвдеениям. Из этих оценок складывается рейтинг.
У произвдений есть жанры, которые может создавать только администратор.
## Технологии
- Python
- Django
- Django REST Framework
- NGINX
- Gunicorn
- Docker
- Docker-compose
## Как запустить 
Клонировать репозиторий себе локально:

``` git clone https://github.com/anastaciakaz/infra_sp2.git ```

Перейти в репозиторий с docker-compose файлом, используя терминал:

``` cd infra_sp2/infra ```

Развернуть докер-контейнеры:

``` docker-compose up -d --build ```

Выполнить миграции и собрать статику:

``` docker-compose exec web python manage.py makemigrations ```

``` docker-compose exec web python manage.py migrate ```

``` docker-compose exec web python manage.py createsuperuser ```

``` docker-compose exec web python manage.py collectstatic --no-input ```

## Создаем дамп базы данных:

``` docker-compose exec web python manage.py dumpdata > dumpPostrgeSQL.json ```

[![Yamdb workflow](https://github.com/anastaciakaz/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?event=push)](https://github.com/anastaciakaz/yamdb_final/actions/workflows/yamdb_workflow.yml)

