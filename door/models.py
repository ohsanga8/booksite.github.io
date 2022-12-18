from django.db import models
from common.models import User
from django.utils import timezone


# 답변 데이터 저장
class AnswerLove(models.Model):
    content = models.TextField()
    class Meta:
        db_table = 'answer_love'

class AnswerMoney(models.Model):
    content = models.TextField()
    class Meta:
        db_table = 'answer_money'

class AnswerFuture(models.Model):
    content = models.TextField()
    class Meta:
        db_table = 'answer_future'

#폼 모델

class Question(models.Model):
    subject = models.CharField(max_length=2)
    question = models.TextField(null=True)

#답변 모델
class Answer(models.Model):
    question= models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateField(default=0000-00-00)


