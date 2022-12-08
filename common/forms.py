from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password")

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': (
            "이름과 비밀번호가 일치하지 않습니다."
        ),
    }

def __init__(self, request=None, *args, **kwargs):
    super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
    self.fields['username'].lable = '이름'
    self.fields['password'].lable = '비밀번호'