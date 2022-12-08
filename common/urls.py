from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', CustomLoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LoginView.as_view(), name='logout'),
]
