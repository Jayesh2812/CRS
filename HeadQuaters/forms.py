from django import forms
from .models import Maindb

class Case_status(forms.ModelForm):
    class Meta:
        model = Maindb
        fields=[
            'db_case_solved'
        ]