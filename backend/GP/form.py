from django import forms
from .models import *
class user(forms.ModelForm) :
    class Meta : 
        model=user
        fields='__all__'

class product(forms.ModelForm) :
    class Meta : 
        model=product
        fields='__all__'