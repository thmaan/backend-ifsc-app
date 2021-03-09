from django import forms
from .models import News

from crispy_forms.helper import FormHelper

class NewsForm(forms.ModelForm):
	class Meta:
		model = News
		fields = [
			'title',
			'introduction',
            'description',
            'tags',
        ]