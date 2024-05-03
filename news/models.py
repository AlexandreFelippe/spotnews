from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.name


def validate_title(value):
    if len(value.split()) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


class News(models.Model):
    title = models.CharField(
        max_length=200, validators=[validate_title], blank=False, null=False
        )
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="news"
    )
    created_at = models.DateField(blank=False, null=False)
    image = models.ImageField(upload_to="img/", blank=True, null=True)
    categories = models.ManyToManyField(
        Category, related_name="news", blank=False
        )

    def __str__(self):
        return self.title
