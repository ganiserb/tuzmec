from django.conf.urls import patterns, url
from servidores import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='servidores-index'),
    )