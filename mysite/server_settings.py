DEBUG = False

STATIC_URL = '/static/'
STATIC_ROOT = '/home/twomoods/twomoods.pythonanywhere.com/mysite/static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
