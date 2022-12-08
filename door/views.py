from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import QuestionForm
from django.utils import timezone

#시작 화면
def start(request):
    return render(request, 'door/start.html')

#분야 선택 & 질문 입력
def question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            question = form.save(commit=False)
            create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'door/question.html')

#결과
def answer(request):
    return render(request, 'door/answer.html')

#이전 문답
def answers(request):
    return render(request, 'door/answer_list.html')