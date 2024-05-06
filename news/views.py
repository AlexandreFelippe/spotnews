from django.shortcuts import render, redirect
from .models import News, Category
from .forms import CreateCategoriesForm, CreateNewsForm


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


def news_form(request):
    form = CreateNewsForm()
    if request.method == "POST":
        form = CreateNewsForm(request.POST, request.FILES)
        if form.is_valid():
            categories = form.cleaned_data.pop("categories").split(",")
            news = News.objects.create(**form.cleaned_data)
            for category in categories:
                news.categories.add(Category.objects.get(name=category))
            return redirect("home-page")
    context = {"form": form}
    return render(request, "news_form.html", context)
