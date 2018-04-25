import string
import random

def randomCode(size=6, chars=string.ascii_lowercase + string.digits):
	return "".join(random.choice(chars) for _ in range(size))

def shortGenerator(instance, size=6):
	code = randomCode(size)
	if instance.__class__.objects.filter(shortenedUrl=code).exists():
		return shortGenerator(instance)
	return code