from django.conf.urls import patterns, include, url

from people import views

urlpatterns = patterns('',
	url(r'^(?P<person_id>\d+)/$', views.person_profile, name='person_profile'),
	url(r'^register/$', views.register_person, name='register_person'),
	url(r'^register/complete-profile/$', views.complete_person_profile, name='complete_person_profile'),
	url(r'^login/$', views.login_person, name='login_person'),
	url(r'^logout/$', views.logout_person, name='logout_person'),
	)