from django import template
from django.http import HttpResponse

from app_slider.models import Slider

register = template.Library()
	
	
@register.inclusion_tag("part_slider.html")
def part_slider():
	slider_entries = Slider.get_all_entries()

	return {
		'slider_entries': slider_entries,
	}	
	
