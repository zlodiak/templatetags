from django import template
from django.contrib.auth.models import User
from django.http import HttpResponse

register = template.Library()
	
	
@register.inclusion_tag("all_docs.html")
def all_docs():
	return {
		'all_docs_entries': 2,
	}	
	


