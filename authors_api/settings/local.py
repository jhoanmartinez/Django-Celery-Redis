
from .base import * # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="m2s5ePE30gwoIezkDxMObr18OCoIMbO0ec-XMgAPE-tQ_aMXik0",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]
