from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Tuzmec.views.home', name='home'),
    # url(r'^Tuzmec/', include('Tuzmec.foo.urls')),

    # Aplicacion de servidores... Por ahora la unica, asi que va como index
    url(r'^$', include('servidores.urls')),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
