from django import forms
from .models import BlogModel


class BlogModelForm(forms.ModelForm):
    class Meta:
        model= BlogModel
        fields = ['title','content','location']
        widgets = {
        'title': forms.TextInput(attrs = {'class':'form-control',}),
        'content': forms.Textarea(attrs = {'class':'form-control'}),
        'location': forms.Select(attrs={'class':'form-control'}),
        }
        
         