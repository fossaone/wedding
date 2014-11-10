from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wedding_website_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^AmyAndNick/', include('AmyAndNick.urls')),
    url(r'^amyandnick/', include('AmyAndNick.urls')),
)
