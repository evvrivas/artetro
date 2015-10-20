"""
Django settings for artetronica project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i(7z+taxo-@6n(qu154^kv@wvywc1=0y8epq-52gtnuy-0ldy8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'artetronica',
    'artetronica.datos_artetronica',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',    
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

ROOT_URLCONF = 'artetronica.urls'

WSGI_APPLICATION = 'artetronica.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
#
#DATABASES = {
#        'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'basetronica5',                  
#        'USER': 'root',             
#        'PASSWORD': 'root',                  
#        'HOST': '',                     
#        'PORT': '',                      
#    }
#}

import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['OPENSHIFT_APP_NAME'],
        'USER': os.environ['OPENSHIFT_MYSQL_DB_USERNAME'],
        'PASSWORD': os.environ['OPENSHIFT_MYSQL_DB_PASSWORD'],
        'HOST': os.environ['OPENSHIFT_MYSQL_DB_HOST'],
        'PORT': os.environ['OPENSHIFT_MYSQL_DB_PORT']
    }
}



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
def rel (*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)),*x)



STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)),  'media')
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'static-only')

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'static'),
)


TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'templates'),
)

#LOGIN_URL = 'mysite_login'
#LOGOUT_URL = 'mysite_logout'
LOGIN_REDIRECT_URL = '/'

AUTH_PROFILE_MODULE = "artetronica.mysiteprofile"

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'