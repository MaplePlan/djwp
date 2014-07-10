from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djwp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^base/api/', include('base.api_urls', namespace='base_api')),
    url(r'^base/page/', include('base.page_urls', namespace='base_page')),
)
