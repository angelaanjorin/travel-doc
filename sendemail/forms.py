from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(
        widget = forms.TextInput(attrs={"placeholder": "Your email"})
    )
    subject = forms.CharField(widget = forms.TextInput(attrs={"placeholder": "Subject"}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "your message"})
    )