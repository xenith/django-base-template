{% if False %}
# Django 1.4 Base Template #

## About ##

This template is based off of the work of [Mozilla Playdoh][playdoh], as well as
experience with other Django layouts/templates. Playdoh is mainly setup for
Mozilla's systems, and is currently only designed for Django 1.3. Some of the
libraries bundled with Playdoh are also no longer necessary in Django 1.4.

This template is designed for Django 1.4's new starproject template option.

As much as I could, all the code has been updated to use the new suggested layout
and functionality in Django 1.4.

[playdoh]: https://github.com/mozilla/playdoh

## How to use this template to create your project ##

- Create your virtualenv
- Install Django 1.4
- django-admin.py startproject --template https://github.com/xenith/django-base-template/zipball/master --extension py,md yourprojectname
- pip install -r projectname/requirements/dev.txt

{% endif %}
# {{ project_name|title }} Project #

Describe your project here.

## Prerequisites ##

- Python >= 2.5
- pip
- virtualenv (virtualenvwrapper is recommended for development)

## Installation ##

Fill out with installation instructions for your project.


License
-------
This software is licensed under the [New BSD License][BSD]. For more
information, read the file ``LICENSE``.

[BSD]: http://opensource.org/licenses/BSD-3-Clause
