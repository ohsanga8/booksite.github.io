from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from common.forms import UserForm

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

#로그인
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'common/login.html', {'error':'username or password is incorrect'})
    else:
        return render(request,'common/login.html')

#로그아웃
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return render(request,'common/logout.html')
