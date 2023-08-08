"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
{% if cookiecutter.admin_panel == 'django-baton' %}
from baton.autodiscover import admin
{% else %}
from django.contrib import admin
{% endif %}
from django.urls import include, path

urlpatterns = [
{% if cookiecutter.admin_panel == 'django-grappelli' %}
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
{% elif cookiecutter.admin_panel == 'django-baton' %}
    path('baton/', include('baton.urls')),
{% endif %}
    path("admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
