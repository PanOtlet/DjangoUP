from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class ServiceSiteMaps(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        # return Entry.objects.filter(is_draft=False)
        return ['index']

    def location(self, item):
        return reverse(item)
        # return None
