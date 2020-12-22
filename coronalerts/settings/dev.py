from coronalerts.settings.base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'coronalerts',
        'USER': 'postgres',
        'PASSWORD': 'vtrCAH5NfSeAhabz5VZm',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
