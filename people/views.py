from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.cache import never_cache
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from people.models import Person
from people.forms import RegisterPersonForm, LoginPersonForm, CompletPersonProfileForm

@login_required
def person_profile(request, person_id):
	"""docs"""

	try:
		person = Person.objects.get(pk=person_id)
	except Person.DoesNotExist:
		raise Http404
	return render(request, 'people/person_profile.html', {'person': person})

@requires_csrf_token
def register_person(request):
	"""
	docx
	"""

	if request.user.is_authenticated():
		return redirect('user_home')
	if request.method == "POST":
		form = RegisterPersonForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'you have been registered successfully, please login to your account')
			return redirect('login_person')
	else:
		form = RegisterPersonForm()

	return render(request, 'people/register_person.html', {'form': form})

@login_required
@requires_csrf_token
def complete_person_profile(request):
	"""
	docx
	"""

	person = request.user
	if person.profile_partially_completed == True:
		return redirect('user_home')

	if request.method == "POST":
		form = CompletPersonProfileForm(request.POST)
		if form.is_valid():
			person.first_name = form.cleaned_data['first_name']
			person.last_name = form.cleaned_data['last_name']
			person.gender = form.cleaned_data['gender']
			person.birthdate = form.cleaned_data['birthdate']
			person.profile_partially_completed = True
			person.profile_completed = True
			person.save(update_fields=['first_name', 'last_name', 'gender', 'birthdate', 'profile_partially_completed', 'profile_completed'])

			messages.success(request, 'completed profile info, thanks.')
			return redirect('user_home')
	else:
		form = CompletPersonProfileForm()

	return render(request, 'people/complete_person_profile.html', {'form': form})

def include_auth_forms(request):
		"""
		docs
		"""

		login_form = LoginPersonForm()
		register_form = RegisterPersonForm()
		return {'login_form': login_form, 'register_form': register_form}

@requires_csrf_token
@never_cache
def login_person(request):
    """
    Displays the login form and handles the login action.
    """
    # redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        form = LoginPersonForm(request, data=request.POST)
        if form.is_valid():

            # Okay, security check complete. Log the user in.
            login(request, form.get_user())
            person = form.get_user()
            if person.profile_partially_completed == False:
            	complete_profile_link = '<a href="%s">Here</a>' % reverse('complete_person_profile')
            	messages.error(request, 'Please complete your profile info to get the best out of MMP %s' % complete_profile_link )

            return redirect('user_home')
    else:
        form = LoginPersonForm(request)

    # current_site = get_current_site(request)

    context = {
        'login_form': form,
        # redirect_field_name: redirect_to,
        # 'site': current_site,
        # 'site_name': current_site.name,
    }
    return render(request, 'people/login_person.html', context)

@login_required
def logout_person(request):
	"""
	docx
	"""

	logout(request)
	return redirect("front_page")