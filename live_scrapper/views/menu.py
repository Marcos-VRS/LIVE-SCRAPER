from django.shortcuts import render


def index(request):
    print("INDEX")
    return render(request, "live_scrapper/index.html")
