from django.db import models

class Answer(models.Model):
    ANSWER_SUBJECTS =  [
        ('LV', '사랑'),
        ('MN', '금전'),
        ('FT', '진로'),
    ]
    question = models.CharField(max_length=50)
    subject = models.CharField(max_length=2, choices=ANSWER_SUBJECTS)
    content = models.TextField()
    create_date = models.DateField()

class AnswerData(models.Model):
    ANSWER_SUBJECTS =  [
        ('LV', '사랑'),
        ('MN', '금전'),
        ('FT', '진로'),
    ]
    subject = models.CharField(max_length=2, choices=ANSWER_SUBJECTS)
    content = models.TextField()
    class Meta:
        db_table = 'answer_data'
