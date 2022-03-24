# class BlogNameForm(forms.Form):
#     length = forms.TextField(label="Password length", widget=forms.Select(choices=CHOICES))
from main.models import Blog
from django import forms


class BlogNameForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name']
