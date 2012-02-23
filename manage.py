#!/usr/bin/env python
import os, sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

    from django.core.management import execute_from_command_line

    # Set a global variable for the project root
    global PROJECT_ROOT
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

    execute_from_command_line(sys.argv)
