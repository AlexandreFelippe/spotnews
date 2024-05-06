from django.shortcuts import render, redirect
from .models import News, Category
from .forms import CreateCategoriesForm


def index(request):
    news = News.objects.all()
    return render(request, "home.html", {"news": news})


def details(request, id):
    news = News.objects.get(id=id)
    return render(request, "news_details.html", {"news": news})


def categories_form(request):
    form = CreateCategoriesForm()
    if request.method == "POST":
        form = CreateCategoriesForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")
    context = {"form": form}
    return render(request, "categories_form.html", context)
