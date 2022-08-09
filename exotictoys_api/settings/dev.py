from .base import *

SECRET_KEY = 'hz3k6i7iu!4^r+=aca3%_if)me7t%a4b6026n4n!ccnp2rw-)q'

DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'