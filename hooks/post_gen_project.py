import os
import shutil
from collections import OrderedDict
from subprocess import run
from venv import create

cookiecutter_string = '''{{ cookiecutter }}'''
cookiecutter: OrderedDict = eval(cookiecutter_string)

project_slug = "{{ cookiecutter.project_slug }}"


class PATH:
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


def create_poetry_env():
    command = ['poetry', 'install']
    run(command)


def create_conda_env():
    command = f'conda env create --file environment.yaml'
    run(command, shell=True)


if cookiecutter['setup_env'] == 'y':
    if cookiecutter['deps_manager'] == 'poetry':
        create_poetry_env()
        PATH.remove(['environment.yaml', "requirements.txt"])
    elif cookiecutter['deps_manager'] == 'pip':
        create_venv()
        PATH.remove(['environment.yaml', "pyproject.toml"])
    elif cookiecutter['deps_manager'] == 'conda':
        create_conda_env()
        PATH.remove(["requirements.txt", "pyproject.toml"])
