from .models import ToDo
from django import forms

class ToDoForm(forms.ModelForm):
    class Meta:
        model=ToDo
        fields=['task','details','status']
    


