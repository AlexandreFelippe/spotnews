from django.shortcuts import render
from .models import News


def index(request):
    news = News.objects.all()
    return render(request, "home.html", {"news": news})


def details(request, id):
    news = News.objects.get(id=id)
    return render(request, "news_details.html", {"news": news})
