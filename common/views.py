from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_view
from .forms import UserForm

#회원가입
def signup_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('question_subject')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request, user)  # 로그인
            return redirect('door.views.question')
    else:
        form = UserForm()
    return render(request, 'common/login.html', {'form': form})


