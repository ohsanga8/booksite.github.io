from django.urls import path
from . import views


urlpatterns = [
    path('', views.start, name='start'),
    path('question/', views.question, name='question'),
    path('answer/', views.answer, name='answer'),
    path('answers/', views.answers, name='answers'),
]
