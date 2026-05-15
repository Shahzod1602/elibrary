from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

CSRF_TRUSTED_ORIGINS = [
    'https://elibrary.autplatform.uz',
    'http://elibrary.autplatform.uz',
]

ENTRA_TENANT_ID = os.getenv('ENTRA_TENANT_ID', '').strip()
ENTRA_CLIENT_ID = os.getenv('ENTRA_CLIENT_ID', '').strip()
ENTRA_CLIENT_SECRET = os.getenv('ENTRA_CLIENT_SECRET', '').strip()
ENTRA_ENABLED = bool(ENTRA_TENANT_ID and ENTRA_CLIENT_ID and ENTRA_CLIENT_SECRET)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'books',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

if ENTRA_ENABLED:
    INSTALLED_APPS.append('django_auth_adfs')
    AUTHENTICATION_BACKENDS.insert(0, 'django_auth_adfs.backend.AdfsAuthCodeBackend')

    AUTH_ADFS = {
        'AUDIENCE': ENTRA_CLIENT_ID,
        'CLIENT_ID': ENTRA_CLIENT_ID,
        'CLIENT_SECRET': ENTRA_CLIENT_SECRET,
        'TENANT_ID': ENTRA_TENANT_ID,
        'RELYING_PARTY_ID': ENTRA_CLIENT_ID,
        'CLAIM_MAPPING': {
            'first_name': 'given_name',
            'last_name': 'family_name',
            'email': 'upn',
        },
        'USERNAME_CLAIM': 'upn',
        'GROUPS_CLAIM': 'roles',
        'MIRROR_GROUPS': True,
        'CREATE_NEW_USERS': True,
    }

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'books.context_processors.footer_categories',
                'accounts.context_processors.entra_status',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

LOGIN_URL = 'django_auth_adfs:login' if ENTRA_ENABLED else 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
