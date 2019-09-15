web: gunicorn astabot.wsgi --log-file -
web: python astabot/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT astabot/settings.py