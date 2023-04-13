from django import forms
from .models import Comment
class EmailForm(forms.Form):
	name=forms.CharField(max_length=50)
	from_email=forms.EmailField()
	to_email=forms.EmailField()
	comment=forms.CharField(widget=forms.Textarea)

class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=['name','email','body']