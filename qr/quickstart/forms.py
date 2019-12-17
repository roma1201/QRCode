from django import forms
from .models import FeedBack

class FeedbackForm(forms.ModelForm):
	text = forms.CharField(widget=forms.Textarea(attrs={"autofocus": "", "placeholder": "Цель вашего визита к нам?"}))
	
	class Meta:
		model = FeedBack
		fields = ['text', 'name', 'contact']