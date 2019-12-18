# django-emailuser #

Use an email address in place of a username in Django.

## motivation ##

As a standard convention for new Django projects, they should begin
with a custom user model, per our [django-practices](https://github.com/lakesite/django-practices). 

* django-emailuser provides a custom user model
* django-emailuser uses AbstractUser to replace username with an email field.

* Area of focus:
  - All django projects.
  - Django apps.

Further [rationale](docs/rationale.md) provided.

## install ##

For installation, please see [install](docs/install.md)

## development ##

To run locally and develop, see [development.md](docs/development.md)

## contributing ##

Please review [standards](docs/standards.md) before submitting issues and pull requests.  Thank you in advance for feedback, criticism, and feature requests.

## example ##

A full example is provided [here](example_project)

## license ##

MIT - See [LICENSE.md](LICENSE.md)
