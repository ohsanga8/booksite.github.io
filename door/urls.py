from django.urls import path
from . import views


urlpatterns = [
    path('', views.start, name='start'),
    path('question/', views.question, name='question_form'),
    path('question/<int:question_id>/', views.answer_create, name='answer_create'),
    path('answer/<int:answer_id>/', views.answer, name='answer'),
    path('answers/', views.answers, name='answers'),
]
