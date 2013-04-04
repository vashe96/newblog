from django import forms
from blog.models import Post
from blog.models import Comment
from django.contrib.auth.models import User


class PostForm(forms.ModelForm): 
    class Meta:
        model = Post         
        exclude = ["author", "created"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]


