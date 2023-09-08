from django.shortcuts import get_object_or_404, redirect, render
from news.models.news_model import News
from news.models.category_model import Categories
from news.forms import CreateCategoriesForm, CreateNewsForm


def home(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def news_details(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(
        request,
        "news_details.html",
        {"news": news, "categories": news.categories.all()},
    )


def categories_form(request):
    form = CreateCategoriesForm()

    if request.method == "POST":
        form = CreateCategoriesForm(request.POST)
        if form.is_valid():
            Categories.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}
    return render(request, "categories_form.html", context)


def news_form(request):
    form = CreateNewsForm()

    if request.method == "POST":
        form = CreateNewsForm(request.POST, request.FILES)

        if form.is_valid():
            # devemos criar o objeto News e adicionar as categorias
            # depois para evitar o erro de criação direta com
            # existência de chave com relacionamento ManyToMany
            form_without_categories = {**form.cleaned_data}
            del form_without_categories["categories"]
            new_news = News(**form_without_categories)
            new_news.save()
            for category in form.cleaned_data["categories"]:
                new_news.add_categories(category)

            return redirect("home-page")

    context = {"form": form}
    return render(request, "news_form.html", context)
