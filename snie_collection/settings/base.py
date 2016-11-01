import os

# Used for internationalization
from django.utils.translation import ugettext_lazy as _

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)
 
SECRET_KEY = get_env_variable('SECRET_KEY')

# Config the base path to look for static and template files
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Config this to be false as default
DEBUG = False

# Setup web server
WSGI_APPLICATION = 'snie_collection.wsgi.application'

# Configure the root url. All url settings is starting from this path.
# Notice: the path is relative to the directory where manage.py is. Because the path of the setting is set up when the virtual env is activated
ROOT_URLCONF = 'snie_collection.urls'


# Application definition

# Most basic apps
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# Utility and helper apps for sites and auth
INSTALLED_APPS += (
    # The Django sites framework is required
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Login via Google and Twitter
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
)

# User defined apps
INSTALLED_APPS += (
    # Installed apps
    'snie_collection.apps.homepage_concept',
    'snie_collection.apps.visualizing_leetcode',
)


# Config middleware (more comments needed)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',

    #include localmiddleware for localization
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)



# Configure database
import dj_database_url
DATABASES = {}
DATABASES['default'] =  dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django_postgrespool'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



# Configue allauth
AUTHENTICATION_BACKENDS = (
    # Default backend -- used to login by username in Django admin
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)


# Used for social media authentification
SITE_ID = 1
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_QUERY_EMAIL = True
LOGIN_REDIRECT_URL = "/"


# Configure TMPLATES. (More comments needs to be added later)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "apps/homepage/sections/poetry/poems"),
            os.path.join(BASE_DIR, "apps/homepage/sections/projects/projects_pages")
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Required by allauth template tags

                # allauth specific context processors
                # Why comment out the following settings: http://stackoverflow.com/questions/31648019/no-module-named-allauth-account-context-processors

                #"allauth.account.context_processors.account",
                #"allauth.socialaccount.context_processors.socialaccount",
            ],
        },
    },
]



# Internationalization, multiple language support
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'
LANGUAGES = (
        ('en', _('English')),
        ('ca', _('Catalan')),
        ('es', _('Spanish')),
    )
LOCALE_PATHS = (
        os.path.join(BASE_DIR, 'locale'),
    )


# TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Configure static file directory
STATIC_ROOT = 'static'

# Look for static files in a folder named static inside each of the apps
STATIC_URL = '/static/'

# Look for static files are used for the whole project and shouldn’t be inside a specific app
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    # Path to shared js and css libs
    os.path.join(BASE_DIR, 'common_static')
)