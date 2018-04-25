from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate(value):
	url_validator = URLValidator()
	invalid = False
	try:
		url_validator(value)
	except:
		http_url = "http://" + value
		try:
			url_validator(http_url)
		except:
			invalid = True
	if invalid:
		raise ValidationError("Invalid URL")
	return value