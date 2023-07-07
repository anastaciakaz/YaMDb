# YAMDB
## Description
This project allows users to leave reviews for their favorite music, songs, movies and books and anything.
Users can follow their favorite browsers, write comments, join groups and, of course, leave their reviews and receive feedback.
Users can also rate works. These ratings form the rating.
The works have genres that only the administrator can create.
## Technologies
- Python
- Django
- Django REST Framework
- NGINX
- Gunicorn
- Docker
- Docker-compose
## How to launch the project 
Clone this repository to your PC:

``` git clone https://github.com/anastaciakaz/infra_sp2.git ```

Go to repository with docker-compose file using terminal:

``` cd infra_sp2/infra ```

Build docker containers:

``` docker-compose up -d --build ```

Run migrations and collect static:

``` docker-compose exec web python manage.py makemigrations ```

``` docker-compose exec web python manage.py migrate ```

``` docker-compose exec web python manage.py createsuperuser ```

``` docker-compose exec web python manage.py collectstatic --no-input ```

## Creating a database dump:

``` docker-compose exec web python manage.py dumpdata > dumpPostrgeSQL.json ```

[![Yamdb workflow](https://github.com/anastaciakaz/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?event=push)](https://github.com/anastaciakaz/yamdb_final/actions/workflows/yamdb_workflow.yml)

