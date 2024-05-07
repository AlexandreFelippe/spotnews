from django.contrib import admin
from .models import News, Category, User

admin.site.register(News)
admin.site.register(Category)
admin.site.register(User)
