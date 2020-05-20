from django import forms

from .models import QAData

class QAForm(forms.ModelForm):


    class Meta:
        model = QAData
        fields = ('context', 'question',)