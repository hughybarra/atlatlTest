from django.conf.urls import patterns, url

from myApp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'test', views.showOwners, name='showOwners')
)