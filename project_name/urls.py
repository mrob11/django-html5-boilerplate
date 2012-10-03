from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Home Page -- Replace as you prefer
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
    if settings.STATIC_ROOT:
        urlpatterns += static(settings.STATIC_URL, 
            document_root=settings.STATIC_ROOT)