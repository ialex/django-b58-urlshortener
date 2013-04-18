from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
'123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.main.views.shortener', name='shortener'),
    url(r'^api/$', 'apps.main.views.api', name='api'),
    url(r'^(?P<hash>[1-9A-HJ-NP-Za-km-z]+)/$', 'apps.main.views.redirect', name='redirect'),
    # url(r'^shortener/', include('shortener.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
