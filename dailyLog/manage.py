#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    if 'DYNO' in os.environ:
        default_settings_file = 'dailyLog.config.production'
    else:
        default_settings_file = 'dailyLog.config.local'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', default_settings_file)
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dailyLog.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
