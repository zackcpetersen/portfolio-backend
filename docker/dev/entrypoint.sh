#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput

# Uncomment below to create a new user
python manage.py createsuperuser --first_name Zack --last_name Petersen --email zackcpetersen@gmail.com --noinput

python manage.py runserver 0.0.0.0:8000

exec "$@"
