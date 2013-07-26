from django.conf.urls import patterns, include, url
from stattracker import views


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stattracker.views.home', name='home'),
    # url(r'^stattracker/', include('stattracker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^team/', include('team.urls', namespace="team")),
    url(r'^player/', include('player.urls', namespace="player")),
    url(r'^', include('home.urls', namespace="home")),
    url(r'^admin/', include(admin.site.urls)),
)
