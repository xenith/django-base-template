from fabric.api import cd, run, env, local, sudo
from lib.fabric_helpers import *
import os
import string


env.hosts = ['{{ project_name }}']
env.code_dir = '/srv/www/{{ project_name }}'
env.virtualenv = '/srv/www/{{ project_name }}/.virtualenv'
env.django_settings_module = '{{ project_name }}.settings'


def run_tests():
    """ Runs the Django test suite as is.  """
    local("./manage.py test")


def deploy_static():
    with cd(env.code_dir):
        run('./manage.py collectstatic -v0 --noinput')


def uname():
    """ Prints information about the host. """
    run("uname -a")


def push():
    "Push new code and pull on all hosts"
    local('git push origin master')
    with cd(env.code_dir):
        run('git pull origin master')


def update_requirements():
    "Update requirements in the virtualenv."
    run("%s/bin/pip install -r %s/requirements/prod.txt" % (env.virtualenv, env.code_dir))


def migrate(app=None):
    """Run the migrate task
    Usage: fab migrate:app_name"""
    if app:
        run("source %s/bin/activate; django-admin.py migrate %s --settings=%s" % (env.virtualenv, app, env.django_settings_module))
    else:
        run("source %s/bin/activate; django-admin.py migrate --settings=%s" % (env.virtualenv, env.django_settings_module))


def deploy():
    push()
    update_requirements()
    migrate()
    run("touch %s/wsgi/django.wsgi" % env.code_dir)
