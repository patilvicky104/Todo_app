from django import forms
from . import models

class uploadForm(forms.ModelForm):
    
    class Meta:
        model = models.TodayList
        fields = ("title","description")
        
