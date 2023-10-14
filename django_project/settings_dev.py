from .settings import *

print("LOADING DEVELOPMENT SETTINGS")
print("=" * 100)


DEBUG = True

INSTALLED_APPS += [
    "django_browser_reload",
    "debug_toolbar",
]

MIDDLEWARE = [  # For dev use only
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # ---------------------------------------------------------
] + MIDDLEWARE


INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
