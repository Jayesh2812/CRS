from django import forms
from HeadQuaters.models import Maindb


class Crime_info_form(forms.ModelForm):
    class Meta:
        model = Maindb
        fields = [
            'db_name',
            'db_ph_no',
            'db_email',
            'db_crime_subject',
            'db_crime_description',
            'db_more_info',
            'db_case_solved',
        ]
        

     