from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    name = forms.CharField
    class Meta:
        model = Author

        fields = ['name',
                  'year_of_birth',
                  'year_of_death',
                  'country_of_origin',
                  ]