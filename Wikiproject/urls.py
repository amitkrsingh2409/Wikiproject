from django.conf.urls import patterns, include, url
from mywiki.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Wikiproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^$', 'mywiki.views.firstpage'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    
    url(r'^delete/(\d+)/$','mywiki.views.delete'),
    url(r'^update/(\d+)/$','mywiki.views.update'),

    url(r'^home/add', 'mywiki.views.homepage'),

    url(r'^api/get_search/', 'mywiki.views.get_search', name='get_search'),

    url(r'^showsearch/', 'mywiki.views.showsearch'),
)
