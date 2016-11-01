#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    # The setting file path is set from the virtual environment varialbles, so the following line is not needed.
    # When deployed to Heroku, a corresponding environment variable on Heroku should be set.

    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "snie_collection.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
