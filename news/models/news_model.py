from django.db import models
from news.validators import validate_date, validation_for_news_title


class News(models.Model):
    title = models.CharField(**validation_for_news_title)
    content = models.TextField()
    author = models.ForeignKey(
        "Users", on_delete=models.CASCADE, related_name="news"
    )
    created_at = models.DateField(validators=[validate_date])
    image = models.ImageField(upload_to="img/", blank=True, null=True)
    categories = models.ManyToManyField("Categories", related_name="news")

    def __str__(self):
        return self.title
