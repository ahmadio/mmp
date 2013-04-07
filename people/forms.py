from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext as _
from django.utils.text import capfirst
from django import forms
from django.forms.extras.widgets import SelectDateWidget

# from people.models import Person


User = get_user_model()

# class RegisterPersonForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     password1 = forms.CharField(label=_("Password"),
#         widget=forms.PasswordInput)
#     password2 = forms.CharField(label=_("Password confirmation"),
#         widget=forms.PasswordInput,
#         help_text=_("Enter the same password as above, for verification."))

#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields = ( "username", "email", "password1", "password2" )


class RegisterPersonForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.

    note copied form the orignal django code with modifications
    """
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'email_registered_before': _("A user with that email already exists."),
        'email_not_correct': _("The email you provided is not valid email."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    email = forms.EmailField(label=_("Email"), max_length=254, required=True)
    username = forms.RegexField(label=_("Username"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username",)

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages['email_registered_before'])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        user = super(RegisterPersonForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class LoginPersonForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = forms.CharField(max_length=254)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': _("Please enter a correct %(username)s and password. "
                           "Note that both fields may be case-sensitive."),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super(LoginPersonForm, self).__init__(*args, **kwargs)

        # Set the label for the "username" field.
        UserModel = get_user_model()
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        if not self.fields['username'].label:
            self.fields['username'].label = capfirst(self.username_field.verbose_name)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'] % {
                        'username': self.username_field.verbose_name
                    })
            elif not self.user_cache.is_active:
                raise forms.ValidationError(self.error_messages['inactive'])
        return self.cleaned_data

    def check_for_test_cookie(self):
        warnings.warn("check_for_test_cookie is deprecated; ensure your login "
                "view is CSRF-protected.", DeprecationWarning)

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache

class PersonChangeForm(UserChangeForm):
    """
    """

    MALE = 'male'
    FEMALE = 'female'
    PERSON_GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        )

    gender = forms.CharField(max_length=7, widget=forms.Select(choices=PERSON_GENDER) ,required=False)
    birthdate = forms.DateField(widget=SelectDateWidget(years=[y for y in range(1900, 2012)]), required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    avatar = forms.ImageField(required=False)
    profile_partially_completed = forms.BooleanField(required=False)
    profile_completed = forms.BooleanField(required=False)

class CompletPersonProfileForm(forms.ModelForm):
    """docstring for CompletPersonProfileForm"""

    MALE = 'male'
    FEMALE = 'female'
    PERSON_GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'gender', 'birthdate')

    first_name = forms.CharField(max_length=254)
    last_name = forms.CharField(max_length=254)
    gender = forms.CharField(max_length=7, widget=forms.Select(choices=PERSON_GENDER))
    birthdate = forms.DateField(widget=SelectDateWidget(years=[y for y in range(1900, 2012)]))





