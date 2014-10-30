from django import template
from django.http import HttpResponse

from app_news.models import News

register = template.Library()
	
	
@register.inclusion_tag("part_last_news.html")
def part_last_news():
	entries_last_news = News.get_last_entries()

	return {
		'entries_last_news': entries_last_news,
	}	
	
