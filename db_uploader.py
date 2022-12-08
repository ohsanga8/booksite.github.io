import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from door.models import AnswerData

CSV_PATH_ANSWER_DATA = './answer_data.csv'

with open(CSV_PATH_ANSWER_DATA, 'rt', encoding='UTF8') as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            subject_data = row[0]
        content_data = row[1]
        AnswerData.objects.create(
            subject = subject_data,
            content = content_data,
        )