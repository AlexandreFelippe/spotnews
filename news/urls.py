from django.urls import path
from .views import index, details, categories_form, news_form

urlpatterns = [
    path("", index, name="home-page"),
    path("/<int:id>", details, name="news-details-page"),
    path("categories", categories_form, name="categories-form"),
    path("news", news_form, name="news-form")
]
