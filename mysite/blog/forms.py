from django import forms
from .models import Post
from profanity_check import predict


class CommentForm(forms.Form):

    comment = forms.CharField(max_length=500, widget=forms.Textarea)

    def clean(self):
        if predict([self.cleaned_data["comment"]]):
            raise forms.ValidationError('Please remove any swear words!')
        return self.cleaned_data
