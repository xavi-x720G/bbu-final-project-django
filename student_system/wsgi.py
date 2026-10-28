"""
WSGI config for student_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_system.settings')

application = get_wsgi_application()

# Automatically collect static files, run database migrations, and setup test data on server startup
# Ensures static files, tables, and demo accounts (admin, teacher, student) always exist on deployment
try:
    call_command('collectstatic', interactive=False, verbosity=0)
    call_command('migrate', interactive=False)
    call_command('setup_test_data', student_count=100, interactive=False)
except Exception as e:
    print(f"Startup setup notice: {e}", file=sys.stderr)
