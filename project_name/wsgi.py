"""
WSGI config for {{ project_name }} project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
#import sys
#import site
#import subprocess


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__) + "../../")

# Add the virtualenv packages to the site directory. This uses the technique
# described at http://code.google.com/p/modwsgi/wiki/VirtualEnvironments

# Remember original sys.path.
#prev_sys_path = list(sys.path)

# Get the path to the env's site-packages directory
#site_packages = subprocess.check_output([
#                    os.path.join(PROJECT_ROOT, '.virtualenv/bin/python'),
#                    '-c',
#                    'from distutils.sysconfig import get_python_lib;'
#                    'print get_python_lib(),'
#]).strip()

# Add the virtualenv site-packages to the site packages
#site.addsitedir(site_packages)

# Reorder sys.path so the new directories are at the front.
#new_sys_path = []
#for item in list(sys.path):
#    if item not in prev_sys_path:
#        new_sys_path.append(item)
#        sys.path.remove(item)
#sys.path[:0] = new_sys_path

# Add the app code to the path
#sys.path.append(PROJECT_ROOT)

os.environ['CELERY_LOADER'] = 'django'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
