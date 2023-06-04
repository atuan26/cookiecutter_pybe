{% if cookiecutter.framework == 'FastAPI' %}
import argparse
import logging
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from {{ cookiecutter.project_slug }}.api import routes
from {{ cookiecutter.project_slug }}.api.deps import get_redis_client
from {{ cookiecutter.project_slug }}.core.config import settings
from {{ cookiecutter.project_slug }}.db.session import add_postgresql_extension


logger = logging.getLogger(__name__)


tags_metadata = [
    {
        "name": "health",
        "description": "Health check for api",
    },
    {
        "name": "memes",
        "description": "Fetch all posts from database",
    },
]

app = FastAPI(
    title="{{ cookiecutter.project_slug }}",
    description="base project for fastapi backend",
    version=settings.VERSION,
    openapi_url=f"/{settings.VERSION}/openapi.json",
    openapi_tags=tags_metadata,
)


async def on_startup() -> None:
    # await add_postgresql_extension()
    # redis_client = await get_redis_client()
    # FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")
    logger.info("FastAPI app running...")


app.add_middleware(CORSMiddleware, allow_origins=["*"])

app.add_event_handler("startup", on_startup)

app.include_router(routes.home_router)
app.include_router(routes.api_router, prefix=f"/{settings.VERSION}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    uvicorn.run(
        'main:app',
        host=args.host,
        port=args.port,
        reload=True,
    )
{% endif %}
{% if cookiecutter.framework == 'Django + FastAPI' %}
import argparse
import os
import sys
import uvicorn


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--host", type=str, default="127.0.0.1")
        parser.add_argument("--port", type=int, default=8000)
        parser.add_argument("--reload", action="store_true")
        args = parser.parse_args()
        uvicorn.run(
            "config.asgi:app",
            host=args.host,
            port=args.port,
            reload=True,
        )
    except:
        """Run administrative tasks."""
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        execute_from_command_line(sys.argv)
{% elif cookiecutter.framework == 'Django' %}
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
{% endif %}

if __name__ == "__main__":
    main()
