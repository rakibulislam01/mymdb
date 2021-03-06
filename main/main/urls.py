"""main URL Configuration

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
from django.contrib.staticfiles.templatetags.staticfiles import static as staticfiles
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from django.utils.translation import ugettext_lazy as _

from material.admin.sites import site

site.site_header = _('mymdb')
site.site_title = _('mymdb')
# site.favicon = staticfiles('/images/favicon.ico')

MEDIA_FILE_PATHS = static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns = [
                  path('admin/', include('material.admin.urls')),
                  # path('admin/', admin.site.urls),
                  path('user/', include('user.urls', namespace='user')),
                  path('', include('movie.urls', namespace='movie')),
              ] + MEDIA_FILE_PATHS

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns = [
#                       path('__debug__/', include(debug_toolbar.urls)),
#
#                       # For django versions before 2.0:
#                       # url(r'^__debug__/', include(debug_toolbar.urls)),
#
#                   ] + urlpatterns
