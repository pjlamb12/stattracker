from django.conf.urls import patterns, url
from player import views


urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^(?P<player_id>\d+)/$', views.detail, name='detail'),
)