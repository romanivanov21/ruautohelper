# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'autohelper',
        'USER': 'my_username',
        'PASSWORD': 'my_password',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
} 