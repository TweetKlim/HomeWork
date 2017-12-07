from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^top/$', views.top, name='top'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^$', views.home, name='home'),
]
