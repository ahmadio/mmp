from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from items.models import Item

def front_page(request):
	"""front page for non-registered user"""

	if request.user.is_authenticated():
		return redirect(user_home)
	else:
		items = Item.objects.all()[:10]
		return render(request, 'home/index.html', {'location': 'home', 'items': items})

@login_required
def user_home(request):
	"""user home view"""

	video_items = Item.objects.filter(type__name='video')
	audio_items = Item.objects.filter(type__name='audio')
	doc_items = Item.objects.filter(type__name='doc')
	return render(request, 'home/user_home.html', {'video_items': video_items, 'audio_items': audio_items, 'doc_items': doc_items})
