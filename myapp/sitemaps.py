from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return ['index', 'services']

    def location(self, item):
        return reverse(item)