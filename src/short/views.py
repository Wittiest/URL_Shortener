from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import shortURL

def newView(request, shortenedUrl=None):
	obj = shortURL.objects.get(shortenedUrl=shortenedUrl)
	return HttpResponse("Shortened: {su}, URL: {real}".format(su=shortenedUrl, real=obj.url))

class NewClassView(View):
	def get(self, request, shortenedUrl=None):
		return HttpResponse("tt")