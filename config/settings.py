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

SAML_BASE_URL = os.getenv('SAML_BASE_URL', 'http://localhost:8000').rstrip('/')
SAML_ENTRA_METADATA_URL = os.getenv('SAML_ENTRA_METADATA_URL', '').strip()
SAML_ENTRA_ENTITY_ID = os.getenv('SAML_ENTRA_ENTITY_ID', '').strip()
SAML_CERT_DIR = BASE_DIR / 'saml_certs'
ENTRA_ENABLED = bool(SAML_ENTRA_METADATA_URL and SAML_ENTRA_ENTITY_ID)

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
    import saml2
    from saml2.saml import NAMEID_FORMAT_EMAILADDRESS

    INSTALLED_APPS.append('djangosaml2')
    AUTHENTICATION_BACKENDS.insert(0, 'djangosaml2.backends.Saml2Backend')
    MIDDLEWARE.append('djangosaml2.middleware.SamlSessionMiddleware')

    SESSION_COOKIE_SECURE = not DEBUG
    SAML_SESSION_COOKIE_NAME = 'saml_session'
    SAML_SESSION_COOKIE_SAMESITE = 'None' if not DEBUG else 'Lax'

    SAML_CREATE_UNKNOWN_USER = True
    SAML_USE_NAME_ID_AS_USERNAME = False
    SAML_DJANGO_USER_MAIN_ATTRIBUTE = 'username'
    SAML_CSP_HANDLER = ''

    SAML_ATTRIBUTE_MAPPING = {
        'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name': ('username',),
        'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress': ('email',),
        'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname': ('first_name',),
        'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname': ('last_name',),
    }

    SAML_CONFIG = {
        'xmlsec_binary': os.getenv('XMLSEC_BINARY', '/usr/bin/xmlsec1'),
        'entityid': f'{SAML_BASE_URL}/saml2/metadata/',
        'allow_unknown_attributes': True,
        'service': {
            'sp': {
                'name': 'AUT E-Library',
                'name_id_format': NAMEID_FORMAT_EMAILADDRESS,
                'endpoints': {
                    'assertion_consumer_service': [
                        (f'{SAML_BASE_URL}/saml2/acs/', saml2.BINDING_HTTP_POST),
                    ],
                    'single_logout_service': [
                        (f'{SAML_BASE_URL}/saml2/ls/', saml2.BINDING_HTTP_REDIRECT),
                        (f'{SAML_BASE_URL}/saml2/ls/post/', saml2.BINDING_HTTP_POST),
                    ],
                },
                'required_attributes': ['emailaddress'],
                'optional_attributes': ['givenname', 'surname', 'name'],
                'allow_unsolicited': True,
                'authn_requests_signed': False,
                'logout_requests_signed': True,
                'want_assertions_signed': True,
                'want_response_signed': False,
            },
        },
        'metadata': {
            'remote': [{'url': SAML_ENTRA_METADATA_URL}],
        },
        'debug': DEBUG,
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

LOGIN_URL = 'saml2_login' if ENTRA_ENABLED else 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
