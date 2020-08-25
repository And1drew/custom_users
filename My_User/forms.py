from My_User.models import custom_user
from django import forms

class login_form(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)


class signup_form(forms.ModelForm):
    class Meta:
        model = custom_user
        fields =['username', 'password', 'displayname', 'age']