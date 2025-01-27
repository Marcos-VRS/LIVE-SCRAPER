from django.urls import path
from live_scrapper import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "live_scrapper"

urlpatterns = [path("index/", views.index, name="index")] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
