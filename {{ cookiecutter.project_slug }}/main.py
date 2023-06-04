#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
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
