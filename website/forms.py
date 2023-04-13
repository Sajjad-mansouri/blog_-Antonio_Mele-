from django import forms

class EmailForm(forms.Form):
	name=forms.CharField(max_length=50)
	from_email=forms.EmailField()
	to_email=forms.EmailField()
	comment=forms.CharField(widget=forms.Textarea)