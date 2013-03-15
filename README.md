{% if False %}
# Django 1.5 Base Template #

## About ##

This template is based off of the work of [Mozilla Playdoh][playdoh] and
[Two Scoops of Django][twoscoops], as well as experience with other Django
layouts/templates. Playdoh is mainly setup for Mozilla's systems, and is
currently only designed for Django 1.4.

This template is designed for Django 1.4's new startproject template option. This version of the template is designed for Django 1.5.

As much as I could, all the code has been updated to use the new suggested layout
and functionality in Django 1.5.

[playdoh]: https://github.com/mozilla/playdoh
[twoscoops]: https://github.com/twoscoops/django-twoscoops-project

## Features ##

By default, this template includes:

A set of basic templates built from HTML5Boilerplate 4.1.0 and Twitter Bootstrap 2.3.1 (located in the
base app)

Templating:

- Markdown
- django_compressor for compressing css/js/less/sass

Security:

- bleach
- python-bcrypt2 - uses bcrypt for password hashing by default

Background Tasks:

- Celery

Migrations:

- South

Caching:

- python-memcached

From Mozilla Playdoh:

- commonware
- nuggets

Admin:

- Includes django-admin-toolbar for development and production (enabled for superusers)
- Includes django-debug-toolbar-user-panel, which is quite useful, but is disabled until it fully supports Django 1.5

Testing:

- nose and django-nose
- pylint, pep8, and coverage

Any of these options can added, modified, or removed as you like after creating your project.

## How to use this template to create your project ##

- Create your working environment and virtualenv
- Install Django 1.5 ($ pip install Django>=1.5)
- $ django-admin.py startproject --template https://github.com/xenith/django-base-template/zipball/master --extension py,md,rst projectname
- $ cd projectname
- Uncomment your preferred database adapter in requirements/compiled.txt (MySQL, Postgresql, or skip this step to stick with SQLite)
- $ pip install -r requirements/local.txt
- $ cp projectname/settings/local-dist.py projectname/settings/local.py (local.py shouldn't be added
  to your source control)
- $ ./manage.py syncdb
- $ ./manage.py runserver

{% endif %}
# {{ project_name|title }} Project #

## About ##

Describe your project here.

## Prerequisites ##

- Python >= 2.6
- pip
- virtualenv (virtualenvwrapper is recommended for use during development)

## Installation ##

Fill out with installation instructions for your project.


License
-------
This software is licensed under the [New BSD License][BSD]. For more
information, read the file ``LICENSE``.

[BSD]: http://opensource.org/licenses/BSD-3-Clause
