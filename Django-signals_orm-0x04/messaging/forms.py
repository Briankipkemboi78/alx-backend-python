from django import forms

class MessageForm(forms.Form):
    receiver_id = forms.IntegerField()  # ID of the receiver
    content = forms.CharField(widget=forms.Textarea, max_length=2000)
