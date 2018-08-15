from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .meta_functions import meta_generator


@cache_page(60*1)
def index(request):
    return render(request, 'service/index.html', {
        'meta': meta_generator('index'),
    }, content_type='text/html')
