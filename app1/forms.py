from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class StudentForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()

    def clea_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError('Please enter a valid email')
        return email
