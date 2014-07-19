from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djwp.views.home', name='home'),

    url(r'^$', views.page_index),
)
