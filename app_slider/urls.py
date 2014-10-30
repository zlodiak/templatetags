from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('app_slider',
	#url(r'^/$', 'views.slider', name='slider'),

)


