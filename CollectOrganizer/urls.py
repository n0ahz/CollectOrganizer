from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Base links:
    url(r'^$', 'CollectOrganizer.views.home', name='home'),
    url(r'^about$', 'CollectOrganizer.views.about', name='about'),
    url(r'^admins$', 'CollectOrganizer.views.admin', name='admin'),
    url(r'^na$', 'CollectOrganizer.views.not_available', name='N/A'),
    # admin shortcut
    url(r'^admin/', include(admin.site.urls)),
    # app links
    url(r'^configs/', include('configs.urls', namespace='configs')),
)
