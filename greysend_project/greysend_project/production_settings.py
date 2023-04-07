import os

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB', 'name'),
            'USER': os.getenv('POSTGRES_USER', 'user'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'password'),
            'HOST': os.getenv('POSTGRES_HOST', 'host'),
            'PORT': '5432',
        }
    }