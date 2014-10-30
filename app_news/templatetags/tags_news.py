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
	

@register.inclusion_tag("part_news.html")
def part_news():
	entries_news = News.get_all_entries()

	return {
		'entries_news': entries_news,
	}	
	