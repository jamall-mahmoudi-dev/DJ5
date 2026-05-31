from django import forms
from .models import Posts

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    status = forms.BooleanField(required=False)
    subject = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    message = forms.CharField(widget=forms.Textarea)


class PostModelForm(forms.ModelForm):
    # custom_field = forms.CharField(max_length=100) 
    class Meta:
        model = Posts
        fields = '__all__'