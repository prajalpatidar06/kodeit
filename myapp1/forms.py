from django import forms
from . models import Blog

class Edit_Blog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('category','title','url','description')

        widgets = {
            'category': forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'url': forms.URLInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }