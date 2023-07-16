from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        
        widgets = {
          'title': forms.TextInput(attrs={'class': 'form-control'}),
          'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
          'author': forms.Select(attrs={'class': 'form-control'}),
          'category': forms.Select(attrs={'class': 'form-control'}),
          'body': SummernoteWidget(),
        }
        
        
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        
        widgets = {
          'title': forms.TextInput(attrs={'class': 'form-control'}),
          'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
          'category': forms.Select(attrs={'class': 'form-control'}),
          'body': SummernoteWidget(),
        }
        