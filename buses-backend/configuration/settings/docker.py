from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'HOST': os.environ['DB_HOST'],
        'USER': os.environ['DB_USER'],
        'PORT': os.environ['DB_PORT'],
        'PASSWORD': os.environ['DB_PASSWORD'],
    }
}