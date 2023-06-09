"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

{% if cookiecutter.framework == 'Django + FastAPI' %}import os

from django.conf import settings
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_asgi_application()


def get_fastAPI_application() -> FastAPI:
    # Main Fast API application
    from apps.polls.routers.choices import router as choices_router
    from apps.polls.routers.questions import router as questions_router

    app = FastAPI()

    # Set all CORS enabled origins
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.ALLOWED_HOSTS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(questions_router)
    app.include_router(choices_router)

    # app.mount(f"/", WSGIMiddleware(application))
    app.mount(f"/", application)

    return app


app = get_fastAPI_application()
{% else %}
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_asgi_application()
{% endif %}