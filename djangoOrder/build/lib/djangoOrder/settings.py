import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'b=3p6y$lr5h@w#pqo%6h0fft$5een3q1=*z$k#oe!vcfu2b&%-'
SECRET_KEY = os.environ['SECRET_KEY']
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['localhost','127.0.0.1','192.168.0.189']
# Application definition
INSTALLED_APPS = [
    'ordersystem',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'djangoOrder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'djangoOrder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


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

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# 로그인후 리다이렉트 페이지는 기본적으로 /accounts/profile 로 지정되어 있는데 이를 변경한다.
LOGIN_REDIRECT_URL = '/index/'

# >>>  장고 서버 적용전 장고의 설정변경 <<<  
# (0)  SECRET_KEY = 'b=3p6y$lr5h@w#pqo%6h0fft$5een3q1=*z$k#oe!vcfu2b&%-' 부분을 
# 환경변수 SECRET_KEY에 등재해주고 
# SECRET_KEY = os.environ['SECRET_KEY'] 와 같이 고친다. 

# (1) DEBUG = False 로 고쳐주고 
# (2) ALLOWED_HOSTS = ['192.168.0.41','localhost','127.0.0.1'] 이와 같이 해주어야 하고 
# (3) 아래 항목을 추가합니다. 
STATIC_ROOT = os.path.join(BASE_DIR,'www_static') # 이는 collectstatic 명령실행시 정적파일들을 한곳으로 모아줌 
# (4) 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/db.sqlite3'), # 이 부분 고치고 
    }
}

# (5) 
'''
 cd /배포프로젝트 
 mkdir db 
 mv db.sqlite3 db/
 chmod 777 db/
 chmod 666 db/db.sqlite3 
 
'''

# (6) 
'''
 cd /배포폴더 
 chmod 777 logs/
 chmod 666 logs/logfile
 
 이외 추가정보 : https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
'''

# (7) 아파치 설치 폴더의 httpd/conf 폴더의 httpd.conf 파일에 mod_wsgi관련설정 추가 (장고교재244페이지참)

SESSION_COOKIE_SECURE = True

LOG_FILE = os.path.join(os.path.dirname(__file__), '../logs', 'myLog.log') 
LOGGING = { 'version': 1, 
'disable_existing_loggers': False, 
'formatters': { 
    'verbose': { 
         'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s", 
         'datefmt' : "%d/%b/%Y %H:%M:%S" }, 
    'simple': { 
            'format': '%(levelname)s %(message)s' }, },
'handlers': { 
    'file': { 'level': 'DEBUG', 'class':     'logging.handlers.RotatingFileHandler',
    'filename': LOG_FILE, 'formatter':'verbose', 
    'maxBytes':1024*1024*10, 
    'backupCount':5, }, }, 
'loggers': { 
    'django': { 'handlers':['file'], 
    'propagate': True, 'level':'INFO', }, 
'django.request': { 
    'handlers':['file'], 'propagate': False, 
    'level':'INFO', }, 
'myAppName': { 
    'handlers': ['file'], 
    'level': 'DEBUG', }, } }


