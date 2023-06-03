import os
import shutil
from collections import OrderedDict
from subprocess import run
from venv import create

cookiecutter_string = '''{{ cookiecutter }}'''
cookiecutter: OrderedDict = eval(cookiecutter_string)

project_slug = "{{ cookiecutter.project_slug }}"


class PATH:
    class FW:
        FASTAPI = [
            os.path.join(project_slug),
            os.path.join('alembic'),
            os.path.join('alembic.ini'),
        ]
        DJANGO = [
            os.path.join("apps", "__init__.py"),
            os.path.join("example"),
            os.path.join("core"),
            os.path.join("staticfiles"),
            os.path.join("manage.py"),
        ]
        DJANGO_AND_FASTAPI = [
            os.path.join("apps", "__init__.py"),
            os.path.join("apps", "polls"),
            os.path.join("polls"),
            os.path.join("config"),
            os.path.join("staticfiles"),
            os.path.join("manage.py"),
        ]
        ALL_FW = list(set(FASTAPI + DJANGO + DJANGO_AND_FASTAPI))

    @classmethod
    def remove(cls, files: list):
        for file in files:
            if os.path.isfile(file):
                os.remove(file)
            else:
                shutil.rmtree(file)


def create_venv():
    requirement_path = os.path.abspath("requirements.txt")
    dir = os.path.join(".venv")
    command = ["bin/pip", "install", "-r", requirement_path]
    create(dir, with_pip=True)
    run(command, cwd=dir)
    PATH.remove(['environment.yaml', "pyproject.toml"])


def create_poetry_env():
    command = ['poetry', 'install']
    run(command)
    run("""cat requirements.txt | grep -E '^[^# ]' | cut -d= -f1 | xargs -n 1 poetry add""", shell=True)
    # PATH.remove(['environment.yaml', "requirements.txt"])


def create_conda_env():
    command = f'conda env create --file environment.yaml'
    run(command, shell=True)
    PATH.remove(["requirements.txt", "pyproject.toml"])


if cookiecutter['setup_env'] == 'y':
    if cookiecutter['deps_manager'] == 'poetry':
        create_poetry_env()
    elif cookiecutter['deps_manager'] == 'pip':
        create_venv()
    elif cookiecutter['deps_manager'] == 'conda':
        create_conda_env()

if cookiecutter['framework'] == 'Django':
    PATH.remove(list(set(PATH.FW.ALL_FW) - set(PATH.FW.DJANGO)))
elif cookiecutter['framework'] == 'FastAPI':
    PATH.remove(list(set(PATH.FW.ALL_FW) - set(PATH.FW.FASTAPI)))
elif cookiecutter['framework'] == 'Django + FastAPI':
    PATH.remove(list(set(PATH.FW.ALL_FW) - set(PATH.FW.DJANGO_AND_FASTAPI)))
