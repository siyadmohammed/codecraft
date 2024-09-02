from django.contrib.sitemaps.views import sitemap
from django.urls import path
from . import views
from .sitemaps import StaticViewSitemap

# Define the sitemaps dictionary
sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]