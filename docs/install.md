# install #

1. Install django-emailuser using pipenv:

    $ pipenv install -e git+https://github.com/lakesite/django-emailuser#egg=django-emailuser

2. Add the app to your settings.py project file, and set the AUTH_USER_MODEL to emailuser.EmailUser:

```
AUTH_USER_MODEL = 'emailuser.EmailUser'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'emailuser',
]
```

3. Run migrations:

    $ python manage.py migrate
