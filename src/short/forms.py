from django import forms

from .validators import validate

class UrlForm(forms.Form):
	    url = forms.CharField(
            label='', 
            validators=[validate],
            widget = forms.TextInput(
                    attrs ={
                        "placeholder": "URL you want to shorten",
                        "class": "form-control"
                        }
                )
		)