from django import forms
from django.contrib.auth.models import User

class MessageForm(forms.Form):
    receiver_id = forms.IntegerField()
    content = forms.CharField(widget=forms.Textarea)
