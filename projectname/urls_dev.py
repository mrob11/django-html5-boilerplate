from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from urls import urlpatterns


urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root':
        settings.MEDIA_ROOT}),
    )
