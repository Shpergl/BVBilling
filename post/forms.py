from django import forms

from post.models import Comments


class CommentsForm(forms.Form):
    class Meta():
        model = Comments
    text = forms.CharField(label='Comment text', max_length=20)
   # article = forms.Field()
