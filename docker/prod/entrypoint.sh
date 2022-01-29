#!/bin/sh

# Migrate
python manage.py migrate
python manage.py collectstatic --noinput

# Start gunicorn server at port 8000
# To watch for code changes, pass the --reload flag to the command
gunicorn portfolio_backend.wsgi:application -b 0.0.0.0:8000
