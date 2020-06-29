from django import forms



class OrderPayForm(forms.Form):
    stripe_token = forms.CharField(max_length=100, widget=forms.HiddenInput)
    address = forms.CharField(max_length=255)
