import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv, find_dotenv
import dj_database_url

# Load environment variables
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
import os
from pathlib import Path

# Try to import dotenv, but don't fail if it's not available
try:
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
except ImportError:
    # dotenv not available, try to load from environment variables directly
    pass

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Rest of your settings...
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, "drainage", "templates")

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-9bv3ge1%z6^itsr^q#$ssef0so*!ex&i#5*e*gg+-^ae9@tgn9")

def get_list(text):
    return [item.strip() for item in text.split(',') if item.strip()]
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = [
    'localhost', 
    '127.0.0.1',
    'bacaca-resort.onrender.com',  # Add this line
]# Application 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'room',
    'api',
    'rest_framework_simplejwt',
     'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_extensions',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "aquasens.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "aquasens.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bacaca_resort_db',
        'USER': 'bacaca_resort_db_user', 
        'PASSWORD': 'jp0EzNrw7HWdLuAfHJoRtcczz19OpxxS',
        'HOST': 'dpg-d1lvf07diees7387g530-a',
        'PORT': '5432',
    }
}

# Authentication
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=365 * 10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=365 * 10),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
}

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# CORS
CORS_ORIGIN_ALLOW_ALL = True

# OAuth / Auth0
AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID", "")
AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET", "")
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN", "")
REDIRECT_URI = os.getenv("REDIRECT_URI", "")

# Primary key type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# Company contact settings
COMPANY_WHATSAPP = "+250786766391"  # Replace with your actual WhatsApp number