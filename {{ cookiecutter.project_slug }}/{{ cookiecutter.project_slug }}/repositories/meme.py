from {{ cookiecutter.project_slug }}.models.meme import Meme
from {{ cookiecutter.project_slug }}.repositories.sqlalchemy import BaseSQLAlchemyRepository
from {{ cookiecutter.project_slug }}.schemas.meme import IMemeCreate, IMemeUpdate


class MemeRepository(BaseSQLAlchemyRepository[Meme, IMemeCreate, IMemeUpdate]):
    _model = Meme
