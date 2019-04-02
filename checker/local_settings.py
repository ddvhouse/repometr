SECRET_KEY = '123456'
DEBUG = True

ALLOWED_HOSTS = ['dev3.repometr.com']

# Override default port for `runserver` command
from django.core.management.commands.runserver import Command as runserver
#runserver.default_addr = '176.99.11.15'
runserver.default_port = '8003'