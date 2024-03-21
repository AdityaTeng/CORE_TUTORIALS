from core.project.settings.custom import IN_DOCKER
from core.project.settings.base import MIDDLEWARE

if IN_DOCKER: # type : ignore
    print('running IN_DOCKER mode')
    assert MIDDLEWARE[:1] == [
        "django.middleware.security.SecurityMiddleware",
    ]
