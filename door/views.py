from django.shortcuts import render
from django.http import HttpResponse

#시작 화면
def start(request):
    return render(request, 'door/start.html')

#분야 선택 & 질문 입력
def question(request):
    return render(request, 'door/question.html')

#결과
def answer(request):
    return render(request, 'door/answer.html')

#이전 문답
def answers(request):
    return render(request, 'door/answer_list.html')