from collections import OrderedDict

cookiecutter_string = '''{{ cookiecutter }}'''
cookiecutter: OrderedDict = eval(cookiecutter_string)


project_slug = "{{ cookiecutter.project_slug }}"
if hasattr(project_slug, "isidentifier"):
    assert project_slug.isidentifier(), "'{}' project slug is not a valid Python identifier.".format(project_slug)