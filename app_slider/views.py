from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from django.template import loader, RequestContext
from django.shortcuts import render, render_to_response

from app_slider.models import Slider


def slider(request):
	"""
	data for render slider page
	"""			
	t = loader.get_template('page_slider.html')
	c = RequestContext(request, {})	
	return HttpResponse(t.render(c)) 