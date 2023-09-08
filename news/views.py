from news.models.news_model import News
from django.shortcuts import get_object_or_404, render


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
