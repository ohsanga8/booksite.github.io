from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import random
from django.utils import timezone

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from door.forms import QuestionForm
from door.models import AnswerLove, AnswerMoney, AnswerFuture, Answer, Question

#시작 화면
def start(request):
    return render(request, 'door/start.html')

#분야 선택 & 질문 입력
def question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question_form = form.save(commit=False)
            question_form.save()
            return redirect('answer_create', question_id=question_form.id)
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'door/question.html')

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #Question 불러오기
    if question.subject == 'LV':
        random_answer = AnswerLove.objects.get(id=random.randrange(1, 50))  # 숫자바꿔
    elif question.subject == 'MN':
        random_answer = AnswerMoney.objects.get(id=random.randrange(1, 50))
    elif question.subject == 'FT':
        random_answer = AnswerFuture.objects.get(id=random.randrange(1, 50))
    answer = Answer(question=question, content=random_answer.content, create_date=timezone.now())
    answer.save()
    return redirect('answer', answer_id=answer.id)
#결과
def answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id) #answer 불러오기
    context = {'answer': answer}
    return render(request, 'door/answer.html', context)

#이전 문답
def answers(request):
    answer_list = Answer.objects.order_by('-create_date')
    context = {'answer_list': answer_list}
    return render(request, 'door/answer_list.html', context)