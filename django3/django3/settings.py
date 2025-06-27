from pathlib import Path

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta - mantenha-a em segredo em produção!
SECRET_KEY = 'django-insecure-(y8(p03g1alpqu41wjy_w6_n1e94_0zpxwoxc1x+b85oh*!x+f'

# Debug - defina como False em produção
DEBUG = True

# Hosts permitidos
ALLOWED_HOSTS = []

# URL de login para redirecionamento de usuários não autenticados
LOGIN_URL = '/crud/login/'

# Aplicações instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crud',  # Certifique-se de que o nome do app está correto
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL de configuração raiz
ROOT_URLCONF = 'django3.urls'  # Substitua 'django3' pelo nome correto do seu projeto

# Configurações de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Adicione o diretório 'templates'
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

# Aplicação WSGI
WSGI_APPLICATION = 'django3.wsgi.application'  # Substitua 'django3' pelo nome correto do seu projeto

# Configuração do banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Certifique-se de que o nome do banco está correto
    }
}

# Validação de senhas
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

# Internacionalização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Adicione o diretório 'static'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Adicione o diretório 'media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
