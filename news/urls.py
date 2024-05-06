from django.urls import path
from .views import index, details

urlpatterns = [
    path("", index, name="home-page"),
    path("/<int:id>", details, name="news-details-page")
]
