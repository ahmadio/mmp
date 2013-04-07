from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext as _

from people.models import Person
from people.forms import PersonChangeForm, RegisterPersonForm

class PersonAdmin(UserAdmin):
	"""docstring for PersonAdmin"""

	fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('email', 'first_name', 'last_name', 'gender', 'birthdate', 'bio', 'avatar', 'profile_partially_completed', 'profile_completed')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
	add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
        ),
    )

	form = PersonChangeForm
	add_form = RegisterPersonForm

admin.site.register(Person, PersonAdmin)
