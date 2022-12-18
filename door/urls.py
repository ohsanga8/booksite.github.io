from django.urls import path
from . import views


urlpatterns = [
    path('', views.start, name='start'),
    path('question/subject', views.question_subject, name='question_subject'),
    path('question/love', views.question_love, name='question_love'),
    path('question/money', views.question_money, name='question_money'),
    path('question/future', views.question_future, name='question_future'),
    path('question/<int:question_id>/', views.answer_create, name='answer_create'),
    path('answer/<int:answer_id>/', views.answer, name='answer'),
    path('answers/', views.answers, name='answers'),
]
