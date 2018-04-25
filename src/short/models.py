from django.db import models
from django.conf import settings

from .validators import validate
from .utils import shortGenerator

#Safer settings import with SHORTURL_SIZE = getattr(settings, "SHORTURL_SIZE", 6)

class ShortURL(models.Model):
	url = models.CharField(max_length = settings.URL_MAX_LEN, validators=[validate])
	shortenedUrl = models.CharField(max_length=settings.SHORTURL_SIZE, unique=True, blank=True)

	def save(self, *args, **kwargs):
		if self.shortenedUrl is None or self.shortenedUrl == "":
			self.shortenedUrl = shortGenerator(self)
		if not "http" in self.url:
			self.url = "http://" + self.url
		super(ShortURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def get_full_url(self):
		return settings.PARENT_URL + '/' + self.shortenedUrl