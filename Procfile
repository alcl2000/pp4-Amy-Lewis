web: gunicorn citizen_detectives.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrat