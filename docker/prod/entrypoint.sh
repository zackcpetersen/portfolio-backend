#!/bin/sh

# Migrate
python manage.py migrate
python manage.py collectstatic --noinput

# Uncomment below to create a new user
#python manage.py createsuperuser --first_name Zack --last_name Petersen --email zack@gmail.com --password admin --noinput

# Start gunicorn server at port 8000
# To watch for code changes, pass the --reload flag to the command
gunicorn portfolio_backend.wsgi:application -b 0.0.0.0:8000
