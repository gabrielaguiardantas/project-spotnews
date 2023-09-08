# playlists/forms.py
from django import forms
from news.models.category_model import Categories
from news.validators import (
    validation_for_categories_name,
    validation_for_news_title,
)
from news.models.user_model import Users


class CreateCategoriesForm(forms.Form):
    name = forms.CharField(**validation_for_categories_name)


class CreateNewsForm(forms.Form):
    title = forms.CharField(**validation_for_news_title, label="Título")
    content = forms.CharField(widget=forms.Textarea, label="Conteúdo")
    author = forms.ModelChoiceField(
        queryset=Users.objects.all(), label="Autoria"
    )
    created_at = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Criado em",
    )
    image = forms.FileField(required=False, label="URL da Imagem")
    categories = forms.ModelMultipleChoiceField(
        queryset=Categories.objects.all(),
        label="Categoria",
        widget=forms.CheckboxSelectMultiple,
    )
