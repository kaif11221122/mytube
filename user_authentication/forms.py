from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField()
    profile_image = forms.ImageField(label='Select a profile icon')
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    test = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "profile_image"]

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        del self.fields['test']
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None
