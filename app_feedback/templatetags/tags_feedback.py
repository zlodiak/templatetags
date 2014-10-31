from django import template
from django.http import HttpResponse
from django import forms

from app_feedback.forms import FeedbackForm

register = template.Library()
	
	
@register.inclusion_tag("part_feedback_modal.html")
def part_feedback_modal():
	form = FeedbackForm()

	return {
		'form': form,
	}	
	
