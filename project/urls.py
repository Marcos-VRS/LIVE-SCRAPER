# No arquivo project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(
        "", include("live_scraper.urls")
    ),  # Conecta a raiz diretamente ao app live_scraper
    path("admin/", admin.site.urls),
]
