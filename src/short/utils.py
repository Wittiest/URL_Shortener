from django.conf import settings

import string
import random

#Safer settings import with SHORTURL_SIZE = getattr(settings, "SHORTURL_MAX_LEN", 6)

def randomCode(size=settings.SHORTURL_SIZE, chars=string.ascii_lowercase + string.digits):
	return "".join(random.choice(chars) for _ in range(size))

def shortGenerator(instance, size=settings.SHORTURL_SIZE):
	code = randomCode(size)
	if instance.__class__.objects.filter(shortenedUrl=code).exists():
		return shortGenerator(instance)
	return code