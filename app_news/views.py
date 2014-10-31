from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from django.template import loader, RequestContext
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from app_news.models import News


def news(request):
	"""
	handler for news tape on separate page
	"""		
	get_all_entries = News.get_all_entries()

	paginator = Paginator(get_all_entries, 6)
	list_pages = paginator.page_range
	
	page = request.GET.get('page')
	try:
		get_all_entries_paginated = paginator.page(page)
	except PageNotAnInteger:
		get_all_entries_paginated = paginator.page(1)
	except EmptyPage:
		get_all_entries_paginated = paginator.page(paginator.num_pages)	
		
	last_page = list_pages[-1]	
	first_page = list_pages[0]		

	t = loader.get_template('custom_news.html')
	c = RequestContext(request, {
		'get_all_entries_paginated': get_all_entries_paginated,
		'list_pages': list_pages,
		'last_page': last_page,
		'first_page': first_page,			
	})	
	
	return HttpResponse(t.render(c)) 		
