from .utils import shortGenerator

from django.db import models

class shortURL(models.Model):
	url = models.CharField(max_length = 260)
	shortenedUrl = models.CharField(max_length=20, unique=True, blank=True)

	def save(self, *args, **kwargs):
		if self.shortenedUrl is None or self.shortenedUrl == "":
			self.shortenedUrl = shortGenerator(self)
		super(shortURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)