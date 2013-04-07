from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from home.views import user_home
from items.models import Item

@login_required
def all_list(request):
	""" """

	return redirect(user_home)

@login_required
def video_list(request):
	""" """

	video_items = Item.objects.filter(type__name='video')
	return render(request, 'items/video_list.html', {'video_items': video_items})

@login_required
def audio_list(request):
	""" """

	audio_items = Item.objects.filter(type__name='audio')
	return render(request, 'items/audio_list.html', {'audio_items': audio_items})

@login_required
def doc_list(request):
	""" """

	doc_items = Item.objects.filter(type__name='doc')
	return render(request, 'items/doc_list.html', {'doc_items': doc_items})

@login_required
def single_video(request, item_id):
	""" """

	single_video = get_object_or_404(Item, pk=item_id, type__name='video')
	return render(request, 'items/single_video.html', {'single_video': single_video})

@login_required
def single_audio(request, item_id):
	""" """

	single_audio = get_object_or_404(Item, pk=item_id, type__name='audio')
	return render(request, 'items/single_audio.html', {'single_audio': single_audio})

@login_required
def single_doc(request, item_id):
	""" """

	single_doc = get_object_or_404(Item, pk=item_id, type__name='doc')
	return render(request, 'items/single_doc.html', {'single_doc': single_doc})

