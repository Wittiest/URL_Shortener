from django.db import models
from django.conf import settings

from .utils import shortGenerator

#Safer settings import with SHORTURL_SIZE = getattr(settings, "SHORTURL_SIZE", 6)

class shortURL(models.Model):
	url = models.CharField(max_length = settings.URL_MAX_LEN)
	shortenedUrl = models.CharField(max_length=settings.SHORTURL_SIZE, unique=True, blank=True)

	def save(self, *args, **kwargs):
		if self.shortenedUrl is None or self.shortenedUrl == "":
			self.shortenedUrl = shortGenerator(self)
		super(shortURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)