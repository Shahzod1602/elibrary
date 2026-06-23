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

# Microsoft Entra ID — OIDC (OpenID Connect) SSO
SSO_BASE_URL = os.getenv('SSO_BASE_URL', 'http://localhost:8000').rstrip('/')
ENTRA_TENANT_ID = os.getenv('ENTRA_TENANT_ID', '').strip()
ENTRA_CLIENT_ID = os.getenv('ENTRA_CLIENT_ID', '').strip()
ENTRA_CLIENT_SECRET = os.getenv('ENTRA_CLIENT_SECRET', '').strip()
ENTRA_SCOPE = os.getenv('ENTRA_SCOPE', 'openid email profile')
ENTRA_REDIRECT_URI = os.getenv('ENTRA_REDIRECT_URI', f'{SSO_BASE_URL}/api/sso/callback')
ENTRA_AUTHORITY = f'https://login.microsoftonline.com/{ENTRA_TENANT_ID}'
ENTRA_METADATA_URL = f'{ENTRA_AUTHORITY}/v2.0/.well-known/openid-configuration'
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

# Production'da (HTTPS) cookie'larni xavfsizlash
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

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

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
