{% if False %}
# Django 1.8 Base Template #

## About ##

This template is based off of the work of [Mozilla Playdoh][playdoh] and
[Two Scoops of Django][twoscoops], as well as experience with other Django
layouts/project templates. Playdoh is mainly setup for Mozilla's systems and is
overly-complicated for a simple project template. (Though it does provide some
very good real-world use examples.)

This project template is designed for Django startproject template option. This version of the
project template is designed for Django 1.8.

As much as I could, all the code has been updated to use the any suggested layouts
and functionality in Django 1.8.

[playdoh]: https://github.com/mozilla/playdoh
[twoscoops]: https://github.com/twoscoops/django-twoscoops-project

## Features ##

By default, this project template includes:

A set of basic templates built from HTML5Boilerplate 4.1.0 and Twitter Bootstrap 3.2.0 (located in the
base app, with css and javascript loaded from CloudFlare CDN by default).

Templating:

- django_compressor for compressing javascript/css/less/sass

Security:

- bleach
- bcrypt - uses bcrypt for password hashing by default

Background Tasks:

- Celery

Migrations:

- Django built-in migrations

Caching:

- python-memcached

Admin:

- Includes django-debug-toolbar for development and production (enabled for superusers)

Testing:

- nose and django-nose
- pylint, pep8, and coverage

Any of these options can added, modified, or removed as you like after creating your project.

## How to use this project template to create your project ##

- Create your working environment and virtualenv
- Make sure you have libffi installed ($ sudo apt-get install libffi-dev)
- Install Django 1.8 ($ pip install Django>=1.8)
- $ django-admin.py startproject --template https://github.com/xenith/django-base-template/zipball/master --extension py,md,rst projectname
- $ cd projectname
- Uncomment your preferred database adapter in requirements/compiled.txt (MySQL, Postgresql, or skip this step to stick with SQLite)
- $ pip install -r requirements/local.txt
- $ cp projectname/settings/local-dist.py projectname/settings/local.py
- $ python manage.py syncdb
- $ python manage.py migrate
- $ python manage.py runserver

That's all you need to do to get the project ready for development. When you deploy your project into production, you should look into getting certain settings from environment variables or other external sources. (See SECRET_KEY for an example.)

There isn't a need to add settings/local.py to your source control, but there are multiple schools of thought on this. The method I use here is an example where each developer has their own settings/local.py with machine-specific settings. You will also need to create a version of settings/local.py for use in production that you will put into place with your deployment system (Fabric, chef, puppet, etc).

The second school of thought is that all settings should be versioned, so that as much of the code/settings as possible is the same across all developers and test/production servers. If you prefer this method, then make sure *all* necessary settings are properly set in settings/base.py, and then edit settings/__init__.py so it no longer reraises the exception. (ie, by replacing 'raise' with 'pass'). As it is, settings/local.py should only be overriding settings from settings/base.py anyway. (You could also just set the DJANGO_SETTINGS_MODULE environment variable to "{{ project_name }}.settings.base" directly.)

## Python 3 compatibility ##

All the code provided in the template itself is compatible with Python 3. Unfortunately, there are still a number of libraries that do not work under Python 3. If you want to use this template under Python 3, you will need to either remove those libraries or find replacements for them.

The libraries I am aware of that do not support Python 3:

* python-memcached (use python3-memcached)

{% endif %}
# The {{ project_name|title }} Project #

## About ##

Describe your project here.

## Prerequisites ##

- Python 2.7, 3.4 recommended
- pip
- virtualenv (virtualenvwrapper is recommended for use during development)

## Installation ##

Fill out with installation instructions for your project.


License
-------
This software is licensed under the [New BSD License][BSD]. For more
information, read the file ``LICENSE``.

[BSD]: http://opensource.org/licenses/BSD-3-Clause
