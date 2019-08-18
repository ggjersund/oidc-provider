"""accounts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.urls import path, include


from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('openid/', include('oidc_provider.urls', namespace='oidc_provider')),
]

urlpatterns += i18n_patterns(
    path('', include('apps.authentication.urls', namespace='authentication')),
    path('', include('apps.account.urls', namespace='account')),
    path('', include('user_sessions.urls', namespace='user_sessions')),
    path('', include(tf_urls, namespace='two_factor')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
