from django.conf.urls import patterns, url
from AmyAndNick import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^rsvp/$', views.rsvp, name='rsvp'),
    url(r'^location/$', views.location, name='location'),
    url(r'^schedule/$', views.schedule, name='schedule'),
    url(r'^accomodations/$', views.accomodations, name='accomodations'),
    url(r'^activities/$', views.activities, name='activities'),
    url(r'^registry/$', views.registry, name='registry'),
    url(r'^bring/$', views.bring, name='bring'),

)