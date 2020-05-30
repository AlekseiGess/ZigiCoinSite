from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['author', 'comment_text']
		labels = {'author': 'Name', 'comment_text': 'Enter your comment'}
		
		