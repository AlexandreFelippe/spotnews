from django import forms
from .models import News


class CreateCategoriesForm(forms.ModelForm):
    name = forms.CharField(max_length=200)


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title', 'content', 'author', 'created_at', 'image', 'categories']
