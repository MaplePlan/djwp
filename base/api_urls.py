from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djwp.views.home', name='home'),

    url(r'^$', views.api_index),
    url(r'^get_site_title/$', 		views.api_get_site_title),
    url(r'^get_site_sub_title/$',	views.api_get_site_sub_title),
    url(r'^get_site_url/$', 		views.api_get_site_url),
    url(r'^get_site_description/$', views.api_get_site_description),
    url(r'^get_site_language/$', 	views.api_get_site_language),
    url(r'^get_os_status/$', 		views.api_get_os_status),
    url(r'^get_djwp_status/$', 		views.api_get_djwp_status),
)
