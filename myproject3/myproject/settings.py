from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


ALLOWED_HOSTS = ['127.0.0.1',
'Fenriz.pythonanywhere.com',
]

STATIC_ROOT = BASE_DIR / 'static/'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp', 'suit',
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

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'admin_static': 'path.to.admin_static',  
            },
        },
    },
]


WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<Fenriz$default>',
        'USER': '<Fenriz>',
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': '<Fenriz.mysql.pythonanywhere-services.com>',
        'OPTIONS': {
'init_command': "SET NAMES 'utf8mb4';"
                "SET sql_mode='STRICT_TRANS_TABLES'",
'               charset': 'utf8mb4',
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SUIT_CONFIG = {
    'ADMIN_NAME': 'Управление магазином', # Название админ-панели
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,
    'LIST_PER_PAGE': 30, # Количество объектов на странице
    'MENU_ICONS': {
        'sites': 'icon-leaf', # Пример иконки
        'auth': 'icon-lock',
    },
    'MENU': (
        # Определение порядка и видимости разделов
        {'label': 'Клиенты', 'icon': 'icon-user', 'models': ('myapp.client',)},
        {'label': 'Товары', 'icon': 'icon-shopping-cart', 'models': ('myapp.product',)},
        {'label': 'Заказы', 'icon': 'icon-shopping-cart', 'models': ('myapp.order',)},
    ),
    'SEARCH_URL': '',
    'MENU_OPEN_FIRST_CHILD': True,
    'MENU_EXCLUDE': ('auth.group',),
    'LIST_DISPLAY': ('__str__',), # Отображаемые поля в списке объектов
}
