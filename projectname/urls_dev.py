from django.conf.urls.defaults import *
from django.conf import settings

from urls import urlpatterns


urlpatterns += patterns('',
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root':
        settings.MEDIA_ROOT}),
    )
