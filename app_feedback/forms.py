from django import forms
from django.forms import ModelForm

from app_feedback.models import Feedback


class FeedbackForm(forms.ModelForm):				
	class Meta:
		model = Feedback
		fields = (
			'author', 
			'subject', 
			'message', 
		)
