"""gil_configuration URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from common.util.util import download
from core import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('homepage.urls', namespace='homepage')),
    url(r'^people/', include('people.urls', namespace='people')),
    url(r'^introduction/', include('introduction.urls', namespace='introduction')),
    url(r'^admissions/', include('admissions.urls', namespace='admissions')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^funding/', include('funding.urls', namespace='funding')),
    url(r'^newsletter/', include('newsletter.urls', namespace='newsletter')),
    url(r'^links/', include('links.urls', namespace='links')),
    url(r'^contactinfo', include('contact_info.urls', namespace='contact_info')),
    url(r'(?P<file>uploads/[\w/.]+)', download, name='download'),
    url(r'^cross_disciplinary/', include('cross_disciplinary.urls', namespace='cross')),
    url(r'^accounts/login/', views.LoginView.as_view(), name='login'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

