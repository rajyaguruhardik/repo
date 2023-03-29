from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '34.18.38.50']

# Configure your local database settings here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ai_algo',
        'USER': 'admin',
        'PASSWORD': '101Market*',
        'HOST': '34.122.177.106',
        'PORT': '5432',
    }
}

# Additional development-specific settings
