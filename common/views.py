from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_view
from common.forms import CustomAuthenticationForm
from .forms import UserForm

#회원가입
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)  # 로그인
            return redirect('door.views.question')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

class CustomLoginView(auth_view.LoginView):
    form_class = CustomAuthenticationForm

