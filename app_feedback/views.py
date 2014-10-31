from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from django.template import loader, RequestContext
from django.shortcuts import render, render_to_response

from app_feedback.models import Feedback


def feedback(request):
	"""
	handler for send feedback message
	"""		
	print('fffed')	

	return 