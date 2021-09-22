from django import forms
from .widgets import CustomClearableFileInput
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'image_url',
            'image',
            'post_title',
            'post_content',
        )

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'comment_title',
            'comment_content',
        )
