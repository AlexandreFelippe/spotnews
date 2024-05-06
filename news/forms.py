from django import forms
from .models import News


class CreateCategoriesForm(forms.Form):
    name = forms.CharField(max_length=200)


class CreateNewsForm(forms.Form):
    categories = forms.CharField(max_length=200, required=False)

    class Meta:
        model = News
        fields = ['title', 'content', 'author', 'created_at', 'image']

    def clean_categories(self):
        categories = self.cleaned_data['categories']
        categories_list = [category.strip() for category in categories.
                           split(',')]
        return categories_list
