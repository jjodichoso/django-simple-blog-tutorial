from django import forms

from django.forms import Textarea, TextInput

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)	
        widgets = {
          'text': Textarea(attrs={'class':'form-control'}),
          'title': TextInput(attrs={'class':'form-control'}),

        }
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
        widgets = {
          'text': Textarea(attrs={'class':'form-control'}),
          'author': TextInput(attrs={'class':'form-control'}),

        }
