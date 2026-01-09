from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': config('MONGO_DB_NAME'),
        'CLIENT': {
            'host': config('MONGO_URI')
        }
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',

    'accounts',
    'registrations',
    'payments',
    'intentions',
]

CORS_ALLOW_ALL_ORIGINS = True
