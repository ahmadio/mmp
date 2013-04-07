from django.conf.urls import patterns, include, url

from home import views

urlpatterns = patterns('',
	url(r'^home$', views.user_home, name='user_home'),
	url(r'^$', views.front_page, name='front_page'),
	)