from django import forms
from . import models


class PostForm(forms.ModelForm):

    class Meta():
        model = models.PostModel
        fields = ('author', 'title', 'text')

        widget = {
            'title': forms.TextInput(attrs = {'class': 'textinputclass'}),
            'text': forms.Textarea(attrs = {'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = models.CommentModel
        fields = ('author', 'text')

        widget = {
            'author': forms.TextInput(attrs = {'class': 'textinputclass'}),
            'text': forms.Textarea(attrs = {'class': 'editable medium-editor-textarea'}),
        }

