# No arquivo live_scraper/urls.py
from django.urls import path
from live_scraper import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "live_scraper"

urlpatterns = [
    path(
        "", views.index, name="index"
    ),  # O índice será acessado diretamente em /live-scraper/
    path("live_darshboard/", views.live_dashboard, name="live_dashboard"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
