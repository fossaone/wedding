from django.conf.urls import patterns, url
from AmyAndNick import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^rsvp/$', views.rsvp, name='rsvp'),
    #url(r'^location/$', views.location, name='location'),
)