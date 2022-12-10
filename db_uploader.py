import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from door.models import AnswerLove, AnswerMoney, AnswerFuture

CSV_PATH_ANSWER_DATA = './answer_data.csv'

with open(CSV_PATH_ANSWER_DATA, 'rt', encoding='UTF8') as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            subject_data = row[0]
        content_data = row[1]
        if subject_data == 'LV':
            AnswerLove.objects.create(
                content = content_data,
            )
        elif subject_data == 'MN':
            AnswerMoney.objects.create(
                content = content_data,
            )
        elif subject_data == 'FT':
            AnswerFuture.objects.create(
                content = content_data,
            )
