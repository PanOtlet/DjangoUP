from django.shortcuts import render
from .meta_functions import meta_generator


def index(request):
    return render(request, 'index.html', {
        'meta': meta_generator('index'),
    })
