from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from django.template import loader, RequestContext
from django.shortcuts import render, render_to_response

from app_feedback.models import Feedback


def feedback(request):
	"""
	handler for send feedback message
	"""		
	if request.method == "GET":
		author = request.GET.get('author', '')	
		subject = request.GET.get('subject', '')	
		message = request.GET.get('message', '')	

		Feedback.objects.create(
			author=author.strip(), 
			subject=subject.strip(), 
			message=message.strip(), 
		)

	return HttpResponseRedirect('/')