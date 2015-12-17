from django import forms

class PostCreationForm(forms.Form):
    post_header = forms.CharField(label='post_header',max_length=200,initial="Post Title")
    post_body = forms.CharField(label='post_body',max_length=500,widget=forms.Textarea,initial="Post Body")