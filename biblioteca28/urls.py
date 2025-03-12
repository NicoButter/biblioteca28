"""
URL configuration for biblioteca28 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from apps.accounts.views import custom_login
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path("admin/", admin.site.urls),
    path('', custom_login, name='home'),
    path('accounts/', include('apps.accounts.urls')),
    path('books/', include('apps.books.urls')),
    path('newspaper/', include('apps.newspaper.urls')),
    path('dashboard/', include('apps.dashboards.urls')),
    path('cardex/', include('apps.cardex.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
