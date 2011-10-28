from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()



urlpatterns = patterns('',
    # url(r'^myapp/', include('myapp.urls')),
    
    # Home Page -- Replace if you like
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
