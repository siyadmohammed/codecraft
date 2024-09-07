
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'autocomplete': 'name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'autocomplete': 'email'
    }))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'autocomplete': 'off'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'autocomplete': 'off'
    }))
