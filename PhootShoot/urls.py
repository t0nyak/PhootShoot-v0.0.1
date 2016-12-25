"""PhootShoot URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from PhootShoot.views import landing_page,login,register
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', landing_page),
	url(r'^user/(register|login)/$', register),
	url(r'^user/$', landing_page),
	url(r'^team/$', landing_page),
	url(r'^team/(\d{1,10})/$', landing_page),
	url(r'^team/stadium/$', landing_page),
	url(r'^team/lineup/$', landing_page),
	url(r'^market/$', landing_page),
	url(r'^competitions/$', landing_page),
	url(r'^league/$', landing_page),
	url(r'^league/(\d{1,8})/$', landing_page),
	url(r'^league/(\d{1,8})/round/(\d{4})/(\d{1,2})/$', landing_page),
	url(r'^player/(\d{1,12})/$', landing_page),
	url(r'^shop/$', landing_page),
	url(r'^payment/$', landing_page),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve'),
]