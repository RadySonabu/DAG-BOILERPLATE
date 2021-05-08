from .base import *

DEBUG = True

INTERNAL_IPS = [
    "127.0.0.1",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(os.path.dirname(BASE_DIR), "db.sqlite3"),
    }
}

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 20,
}
CORS_ORIGIN_ALLOW_ALL = True
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
