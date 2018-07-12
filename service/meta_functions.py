from meta.views import Meta
from .models import SEOMeta
from django.conf import settings


def meta_generator(route_name: str):
    try:
        seo = SEOMeta.objects.get(website=route_name)
        meta = Meta(
            title=seo.title,
            description=seo.meta_description,
            keywords=seo.keywords.split(','),
        )
    except SEOMeta.DoesNotExist:
        meta = Meta(
            title=settings.META['title'],
            description=settings.META['description'],
            keywords=settings.META['keywords']
        )

    meta.extra_custom_props = [
        ('http-equiv', 'Content-Type', 'text/html; charset=UTF-8'),
    ]
    meta.extra_props = {
        'viewport': 'width=device-width, initial-scale=1.0, minimum-scale=1.0'
    }

    return meta
