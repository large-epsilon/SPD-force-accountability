# SPD Use of force accountability

Website to show individual officer's use of force history on demand.

## Installation:

First, install Docker and docker-compose if you don't have them already.

In the root directory of this repo:
```
$ docker-compose build
$ docker-compose up -d
$ docker-compose exec web python manage.py migrate --noinput
```

Then, to make the site useful, you need to upload some data to it. First, make
an admin account:
```
$ docker-compose exec web python manage.py createsuperuser
```

Then navigate to `/admin/officer_history/incidents/upload_csv/`, log in, and
follow the instructions there.
