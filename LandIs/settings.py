"""
Django settings for LandIs project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

# from pathlib import Path
import os

# from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j^5oh%l-(#4lsu63xhkuyogu!i&)untvwd430uhcvb4kvi70(l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_HOST_USER = 'sambulikevin@gmail.com'
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # EMAIL_HOST = 'smtp.gmail.com'
    # EMAIL_HOST_USER = 'sambulikevin@gmail.com'
    # EMAIL_HOST_PASSWORD = 'kevoh1995'
    # EMAIL_USE_TLS = True
    # EMAIL_PORT = 587
    # DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
else:
    EMAIL_HOST = 'smtp.mailgun.org'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'postmaster@sandboxbc8f324eb8104fea958b1b95394167c9.mailgun.org'
    EMAIL_HOST_PASSWORD = 'f6d094eddcd50e8df6476ab79ddcf554-71b35d7e-786f6a53'
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ALLOWED_HOSTS = ['https://rundalis.herokuapp.com/', '0c08c280dc9d.ngrok.io', '127.0.0.1', 'localhost']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': 'LandIs',
#         'USER': 'postgres',
#         'HOST': 'localhost',
#         'PASSWORD': 'kevoh',
#         'PORT': '5432'
#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'd5raml675lgp88',
        'USER': 'sqdrtjajozetcu',
        'HOST': 'ec2-18-214-208-89.compute-1.amazonaws.com',
        'PASSWORD': '70cab36a0742c993927838fbc8a578d3e0859fba762d2eb09e02be0357ccb2ef',
        'PORT': '5432'
    },
}


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # GIS modules
    'django.contrib.gis',
    'leaflet',
    'djgeojson',

    # personal apps
    'accounts',
    'parcels',
    'ownership',
    'transaction',
    'payments',

    'social_django',
    'rest_framework',
    'rest_framework.authtoken',
    # 'nairobi_hospitals_api',
    # 'crispy_forms',
]

AUTH_USER_MODEL = 'accounts.Account'

# CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'social_django.middleware.SocialAuthExceptionMiddleware',
]

# MESSAGE_TAGS = {
#     messages.DEBUG: 'alert-info',
#     messages.INFO: 'alert-info',
#     messages.SUCCESS: 'alert-success',
#     messages.WARNING: 'alert-warning',
#     messages.ERROR: 'alert-danger',
# }

ROOT_URLCONF = 'LandIs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # 'social_django.context_processors.backends',
                # 'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'LandIs.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, '/static'),)
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-1.22488, 36.827164),
    'DEFAULT_ZOOM': 16,
    'MAX_ZOOM': 20,
    'MIN_ZOOM': 14,
    'SCALE': 'both',
    'MINIMAP': True,
    'ATTRIBUTION_PREFIX': 'Map by Kevin Sambuli Amuhaya',
    'TILES':
        [('Satellite', 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
          {'maxZoom': 19,
           'attribution': '&copy; <a ''href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}),

         ('Topography', 'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
          {'maxZoom': 17,
           'attribution': 'Map data: &copy; <a' 'href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
                          'contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a '
                          'href="https://opentopomap.org">OpenTopoMap</a> (<a '
                          'href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'}),

         ('Stamen Toner', 'https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}{r}.{ext}', {
             'attribution': 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, '
                            '<a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data '
                            '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
             'subdomains': 'abcd', 'minZoom': 0, 'maxZoom': 20, 'ext': 'png'
         }),

         ('Terrain', 'https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}', {
             'maxZoom': 20,
             'attribution': 'Tiles courtesy of the <a href="https://usgs.gov/">U.S. Geological Survey</a>'
         }),
         ]

}

# SERIALIZATION_MODULES = {
#     'geojson': 'djgeojson.serializers'
# }

#
SERIALIZATION_MODULES = {
    "geojson": "django.contrib.gis.serializers.geojson",
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

# GEOIP_PATH = os.path.join(BASE_DIR, 'geoip')
# GEOIP_CITY = os.path.join(BASE_DIR, 'geoip/GeoLite2-City')
# GEOIP_COUNTRY = os.path.join(BASE_DIR, 'geoip/GeoLite2-Country')

# try:
#     from django_shop.local_settings import *
# except ImportError:
#     pass
