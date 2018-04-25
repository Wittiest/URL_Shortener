from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .forms import UrlForm
from .models import ShortURL

class IndexView(View):
	def get(self, request, *args, **kwargs):
		form = UrlForm()
		context = {
			'title': "URL Shortener",
			'form': form
		}
		return render(request, 'index.html', context)
	def post(self, request, *args, **kwargs):
		form = UrlForm(request.POST)
		context = {
			'title': "URL Shortener",
			'form': form
		}
		temp = 'index.html'
		if form.is_valid():
			obj, created = ShortURL.objects.get_or_create(url=form.cleaned_data.get("url"))
			context = {
				'object': obj,
				'created': created,
			}
			if created:
				temp = 'created.html'
			else:
				temp = 'exists.html'
		return render(request, temp, context)

class NewView(View):
	def get(self, request, shortenedUrl=None):
		obj = get_object_or_404(ShortURL, shortenedUrl = shortenedUrl)
		return HttpResponseRedirect(obj.url)
