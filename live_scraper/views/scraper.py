from django.shortcuts import render


def live_dashboard(request):
    return render(request, "live_scraper/live_dashboard.html")
