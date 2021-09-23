from .base import *

env_list = dict()

local_env = open(os.path.join(BASE_DIR, '.env'))

while True :
    line = local_env.readline()
    if not line :
        break
    line = line.replace('\n', '')
    start = line.find('=')
    key = line[:start]
    value = line[start+1:]
    env_list[key] = value

def read_secrets(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secrets('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': read_secrets('MARIADB_USER'),
        'PASSWORD': read_secrets('MARIADB_PASSWORD'),
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}