#!/bin/bash
# entrypoint.sh file of Dockerfile
# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput
# Apply database migrations
echo "Apply database migrations"
python manage.py migrate
python manage.py makemigrations
# Start server
echo "Starting server"
