from django.shortcuts import (
    render
)

from .models import Post


def view_explore(request):
    """ Returns explore.html """
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'explore/explore.html', context)
