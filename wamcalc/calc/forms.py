from django import forms

from .models import Marks


class EditMarkForm(forms.ModelForm):
    name = forms.CharField()
    code = forms.CharField()
    mark = forms.DecimalField()
    cp = forms.IntegerField()

    class Meta:
        model = Marks
        fields = [
            'name',
            'code',
            'mark',
            'cp'
        ]
        
