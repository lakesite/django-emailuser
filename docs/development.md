# development #

Extending and developing emailuser is best done through the included example
django project.  

## setup ##

Using pipenv:

        $ cd example_project
        $ pipenv install --ignore-pipfile
        (django-emailuser) $ python manage.py migrate
        (django-emailuser) $ python manage.py createsuperuser
        (django-emailuser) $ python manage.py runserver

## using ##

        (django-emailuser) $ python manage.py createsuperuser
        (django-emailuser) $ python manage.py runserver

The default Django system with emailuser app is accessible at:

    http://localhost:8000/admin/

## testing ##

        $ cd example_project
        $ python manage.py test
