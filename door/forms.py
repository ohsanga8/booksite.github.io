from django import forms
from door.models import Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question', 'subject']