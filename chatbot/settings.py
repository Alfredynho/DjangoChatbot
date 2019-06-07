import os
from os.path import join, dirname

PROJECT_PATH = dirname(dirname(dirname(__file__)))
APPS_PATH = join(PROJECT_PATH, "apps")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'h#srg0%!#)fdct779*0e7kzich#qaq-4c&0k25#2%4w(gz20u8'

DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.messenger',
    'apps.author',
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

ROOT_URLCONF = 'chatbot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'templates')],
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

WSGI_APPLICATION = 'chatbot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Configuraciones del Chatbot

CLIENT_ACCESS_TOKEN_DIALOG_FLOW = "c004deae54af4395be77391236c6e6cc"
FB_PAGE_ACCESS_TOKEN = "EAADRuExI5U0BAMnCzSydhAZCWDvNlrczX9DHdZCCwbcewtNmOvjtpuO0qxVLKMFVpFEh28b9d4LigYZCn8L6YBJsrliIKULrVkzCEzZAcB4KtbMoUy97Pba8jLPmeXUiNYB4xzNZAZCiWY6jHonG33zxVx5OnXKq5ooG4MwzZBjopPM8GxJZB9Lm"


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)



# Config Constance for Project Chatbot
CONSTANCE_CONFIG = {
    'CLIENT_ACCESS_TOKEN_DIALOG_FLOW': ('','Copiar el Access Token del Agente de Dialog Flow, '
                       'DIALOG FLOW'),
    'FB_PAGE_ACCESS_TOKEN': ('','Copiar el Access Token de la pagina de Facebook, '
                       'PAGES ACCES TOKEN FB'),      

    'VERIFY_TOKEN': ('','Colocar el verify Token para conectar FBDV con el backend, '
                       'FBDV'),    
}