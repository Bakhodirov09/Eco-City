from data.config import env

DB_NAME = env.str('DB_NAME')
DB_PASS = env.str('DB_PASS')
DB_HOST = env.str('DB_HOST')
DB_PORT = env.str('DB_PORT')
DB_USER = env.str('DB_USER')

I18N_DOMAIN = 'lang'
LOCALES_DIR = 'locale'