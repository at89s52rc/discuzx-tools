"""govern URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from admin_honeypot import urls as honeypot_urls
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.admindocs import urls as admindocs_urls

# from filebrowser.sites import site

# import xadmin
# from xadmin.plugins import xversion

# xadmin.autodiscover()
# xversion.register_models()

admin.autodiscover()

urlpatterns = [
    # url(r'^govern/xadmin/', include(xadmin.site.urls)),
    # url(r'^govern/filebrowser/', include(site.urls)),
    url(r'^govern/grappelli/', include('grappelli.urls')),
    url(r'^govern/superman/doc/', include(admindocs_urls)),
    url(r'^govern/superman/', include(admin.site.urls)),
    url(r'^govern/admin/', include(honeypot_urls, namespace='admin_honeypot')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns(
        '', url(r'^__debug__/', include(debug_toolbar.urls)), )
