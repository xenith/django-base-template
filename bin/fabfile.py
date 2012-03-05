from fabric.api import cd, run, env, local, sudo, require
from fabric.operations import _prefix_commands, _prefix_env_vars
from lib.fabric_helpers import *
import os
import string


env.hosts = ['{{ project_name }}.example.com']
env.code_dir = '/srv/www/{{ project_name }}'
env.virtualenv = '/srv/www/{{ project_name }}/.virtualenv'
env.code_repo = 'git@github.com:user/{{project_name}}.git'
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
    """ Push new code and pull on all hosts """
    local('git push origin master')
    with cd(env.code_dir):
        run('git pull origin master')


def update_requirements():
    """ Update requirements in the virtualenv. """
    run("%s/bin/pip install -r %s/requirements/prod.txt" % (env.virtualenv, env.code_dir))


def migrate(app=None):
    """
    Run the migrate task
    Usage: fab migrate:app_name
    """
    if app:
        run("source %s/bin/activate; django-admin.py migrate %s --settings=%s" % (env.virtualenv, app, env.django_settings_module))
    else:
        run("source %s/bin/activate; django-admin.py migrate --settings=%s" % (env.virtualenv, env.django_settings_module))


def version():
    """ Show last commit to the deployed repo. """
    with cd(env.code_dir):
        run('git log -1')


def restart():
    """ Restart the wsgi process """
    with cd(env.code_dir):
        run("touch %s/{{ project_name }}/wsgi.py" % env.code_dir)


def ve_run(cmd):
    """
    Helper function.
    Runs a command using the virtualenv environment
    """
    require('root')
    return sshagent_run('source %s/bin/activate; %s' % (env.virtualenv, cmd))


def sshagent_run(cmd):
    """
    Helper function.
    Runs a command with SSH agent forwarding enabled.

    Note:: Fabric (and paramiko) can't forward your SSH agent.
    This helper uses your system's ssh to do so.
    """
    # Handle context manager modifications
    wrapped_cmd = _prefix_commands(_prefix_env_vars(cmd), 'remote')
    try:
        host, port = env.host_string.split(':')
        return local(
            "ssh -p %s -A %s@%s '%s'" % (port, env.user, host, wrapped_cmd)
        )
    except ValueError:
        return local(
            "ssh -A %s@%s '%s'" % (env.user, env.host_string, wrapped_cmd)
        )


def deploy():
    """ Update the remote deployment, update the virtualenv, perform any
    pending migrations, then restart the wsgi process """
    push()
    update_requirements()
    migrate()
    restart()


def clone():
    """ Clone the repository for the first time """
    with cd(env.code_dir):
        run('git clone %s .' % (env.code_repo))


def bootstrap():
    """ Bootstrap the initial deploy environment, then deploy """
    run('mkdir %s' % (env.code_dir))
    run('virtualenv %s' % (env.virtualenv))
    clone()
    deploy()
