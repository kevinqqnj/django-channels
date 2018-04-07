# django-channels
channels tutorial running in docker
http://channels.readthedocs.io/en/latest/tutorial/index.html

## how to run
- git clone
- docker-compose up --build

open Web browser at http://localhost:5000

## Worker for background tasks
This command handles HTTP and WebSocket protocols
`python manage.py runserver 0.0.0.0:5000`

This command creates a worker to run background task
python manage.py runworker thumbnails-generate
