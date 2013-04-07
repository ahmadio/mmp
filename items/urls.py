from django.conf.urls import patterns, include, url

from items import views

urlpatterns = patterns('',
	url(r'^$', views.all_list, name='all_list'),
	url(r'^video/$', views.video_list, name='video_list'),
	url(r'^audio/$', views.audio_list, name='audio_list'),
	url(r'^doc/$', views.doc_list, name='doc_list'),
	url(r'^video/(?P<item_id>\d+)/$', views.single_video, name='single_video'),
	url(r'^audio/(?P<item_id>\d+)/$', views.single_audio, name='single_audio'),
	url(r'^doc/(?P<item_id>\d+)/$', views.single_doc, name='single_doc'),
	)