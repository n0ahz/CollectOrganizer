from django.conf.urls import patterns, include, url
from configs import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^navigator/$', views.navigator, name='navigator'),
)
