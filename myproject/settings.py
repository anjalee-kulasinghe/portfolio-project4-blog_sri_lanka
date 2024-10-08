import os
import dj_database_url
from pathlib import Path

# Load environment variables from .env (if using python-dotenv)
from dotenv import load_dotenv
load_dotenv()

# Import environment variables if env.py exists
if os.path.isfile('env.py'):
    import env

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

SECRET_KEY = os.environ.get("SECRET_KEY", "9k<jR4Ue$o$i@k=")
DEBUG = True

ALLOWED_HOSTS = [
    '.herokuapp.com',
    'localhost',
    '8000-anjaleekula-portfoliopr-k2fv7empuq1.ws.codeinstitute-ide.net',
    '.gitpod.io',
    '*.ws.codeinstitute-ide.net',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default authentication backend
]

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_summernote",
    "blog",
    "users",
    "corsheaders",
    "crispy_forms",
    "crispy_bootstrap5",
    "tinymce",
    "cityguide",
    "food",
    "traveltips",
    "contact",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TINYMCE_DEFAULT_CONFIG = {
    'height': 500,
    'plugins': 'advlist autolink lists link image charmap preview anchor searchreplace visualblocks code fullscreen insertdatetime media table paste code help wordcount',
    'toolbar': 'undo redo | formatselect | bold italic backcolor | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | removeformat | help',
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database configuration with debugging
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///db.sqlite3")
print(f"DATABASE_URL: {DATABASE_URL} (type: {type(DATABASE_URL)})")  # Debugging
if isinstance(DATABASE_URL, bytes):
    DATABASE_URL = DATABASE_URL.decode('utf-8')
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL)
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CSRF_TRUSTED_ORIGINS = [
    'https://*.gitpod.io',
    'https://8000-anjaleekula-portfoliopr-f9awqdmbr60.ws.codeinstitute-ide.net',
    'https://*.ws.codeinstitute-ide.net',
]

CSRF_COOKIE_SECURE = False

CORS_ALLOWED_ORIGINS = [
    'https://8000-anjaleekula-portfoliopr-f9awqdmbr60.ws.codeinstitute-ide.net',
    'https://*.gitpod.io',
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'login'

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'