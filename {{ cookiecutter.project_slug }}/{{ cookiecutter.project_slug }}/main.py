import logging

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
