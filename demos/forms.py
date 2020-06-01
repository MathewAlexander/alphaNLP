from django import forms

from .models import QAData

class QAForm(forms.ModelForm):


    class Meta:
        model = QAData
        fields = ('context', 'question',)
    def __init__(self, *args, **kwargs):
            super(QAForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
            self.fields['context'].widget.attrs['cols'] = 100
            self.fields['context'].widget.attrs['rows'] = 5
            self.fields['question'].widget.attrs['cols'] = 40
            self.fields['question'].widget.attrs['rows'] = 1